from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import ServicesPost, Category, ServiceLike
from .form import Comments, CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from ..main.models import Services


class ServicesListView(View):
    template_name = 'services/service_list.html'

    def get(self, request, *args, **kwargs):
        services = ServicesPost.objects.order_by('-id')
        services_3 = ServicesPost.objects.order_by('-id')[:3]
        categories = Category.objects.all()
        category = self.request.GET.get('category')
        if category:
            services = services.filter(category__name__exact=category)
        paginator = Paginator(services, 3)
        page = self.request.GET.get('page')
        services = paginator.get_page(page)
        ctx = {
            'object_list': services,
            'services_3': services_3,
            'categories': categories
        }
        return render(request, self.template_name, ctx)


def service_detail(request, slug):
    service_3 = ServicesPost.objects.order_by('-id')[:3]
    blog = get_object_or_404(ServicesPost, slug=slug)
    categories = Category.objects.all()
    comments = Comments.objects.filter(blog=blog, parent__isnull=True).order_by('-id')
    form = CommentForm()
    cid = request.GET.get('cid')
    if request.method == 'POST':
        form = CommentForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blog
            obj.author = request.user
            if cid:
                obj.parent_id = cid
            obj.save()
            messages.success(request, 'You have successfully commentary')
            return redirect(f'.#comment-{obj.id}')
    context = {
        'blog': blog,
        'service_3': service_3,
        'categories': categories,
        'comments': comments,
        'form': form

    }
    return render(request, 'services/service_detail.html', context)


class LikeRedirectView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account:login')

    def get(self, request, *args, **kwargs):
        eid = self.kwargs.get('eid')
        path = request.GET.get('next')
        if request.user.servicelike_set.filter(blog_id=eid).exists():
            request.user.servicelike_set.filter(blog_id=eid).delete()
            messages.success(request, 'disliked')
        else:
            ServiceLike.objects.create(author_id=request.user.id, blog_id=eid)
            messages.success(request, 'liked')
        return redirect(path)