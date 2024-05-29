from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from apps.rooms.models import Room, Image, Booking
from .form import RoomForm
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User


def room_list(request):
    rooms = Room.objects.all()
    page = request.GET.get('page',)
    check_in = request.GET.get('checkin-date')
    check_out = request.GET.get('checkout-date')
    max_adults = request.GET.get('adults')
    max_children = request.GET.get('children')
    price = request.GET.get('price')
    room_number = request.GET.get('room_number')
    if check_in and check_out:
        rooms = rooms.filter(~Q(rooms_booking__check_in__lte=check_out) | ~Q(rooms_booking__check_out__gte=check_in))
        if int(room_number) != 0:
            rooms = rooms.filter(Q(room_number1__exact=room_number))
        if int(max_adults) != 0 or int(max_children) != 0:
            rooms_max_person = rooms.filter(Q(max_person=int(max_adults)+int(max_children)))
            rooms = rooms.intersection(rooms_max_person)
        messages.info(request, f'numbers of rooms fount {rooms.count()}')
    paginator = Paginator(rooms, 3)
    page_obj = paginator.get_page(page)
    cnt = {
        'object_list': page_obj,
    }
    return render(request, 'rooms/room.html', cnt)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    form = RoomForm()
    ctx = {
    }
    if request.method == 'POST':
        check_in = '20'+'-'.join(request.POST['check_in'].split('/')[::-1])
        check_out = '20' + '-'.join(request.POST['check_out'].split('/')[::-1])
        data = {
            'check_in': check_in,
            'check_out': check_out,
        }
        farq = abs((datetime.strptime(check_out, '%Y-%m-%d') - datetime.strptime(check_in, '%Y-%m-%d')).days)
        ctx['farq'] = farq
        form = RoomForm(data)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.room = room
            obj.author_id = request.user.id
            form.save()
            messages.success(request, f'You booked the room for {farq} days and the total price $={farq*room.price}')
            return redirect('.')
        else:
            messages.success(request, 'the room is booking!!!')
            return redirect('/')
    ctx = {
        'room': room,
        'form': form,
    }
    return render(request, 'rooms/single-room.html', ctx)
