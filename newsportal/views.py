from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from .filters import CommFilter
from .models import *
from .forms import *


class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'PostList.html'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'PostCreate.html'
    raise_exception = True

    def form_valid(self, fors):
        post = fors.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(fors)


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'detailes.html'


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('newsportal.change_message')
    model = Post
    form_class = PostForm
    template_name = 'PostCreate.html'


class PostDel(PermissionRequiredMixin, DeleteView):
    permission_required = ('newsportal.delete_message')
    model = Post
    template_name = 'PostDelete.html'
    success_url = 'http://127.0.0.1:8000/messages/'


class MyCommentList(ListView):
    model = Comment
    template_name = 'MyCommentList.html'
    context_object_name = 'MyCommentList'
    ordering = '-dateComm'

    def get_queryset(self):
        queryset = Comment.objects.filter(message__author__id=self.request.user.id)
        self.filterset = CommFilter(self.request.GET, queryset, request=self.request.user.id)
        if not self.request.GET:
            return Comment.objects.none()
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['get'] = self.request.GET
        return context


class CommCreate(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommForm
    raise_exception = True
    template_name = 'CommCreate.html'

    def form_valid(self, fors):
        comment = fors.save(commit=False)
        comment.author = self.request.user
        comment.message_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(fors)


@login_required
def profile(request, pk=None):
    if pk:
        post_owner = get_object_or_404(User, pk=pk)
        user_posts = Post.objects.filter(author_id=request.user).order_by('-dateMsg')

    else:
        post_owner = request.user
        user_posts = Post.objects.filter(author_id=request.user).order_by('-dateMsg')
    return render(request, 'profile.html', {'post_owner': post_owner, 'user_posts': user_posts})


def comment(request, pk):
    queryset = Comment.objects.filter(message=pk).order_by('-dateComm')
    return render(request,'CommDet.html',{'CommDet': queryset})


class OneComm(DetailView):
    model = Comment
    context_object_name = 'OneComm'
    template_name = 'OneComm.html'


class CommDel(PermissionRequiredMixin, DeleteView):
    permission_required = 'newsportal.delete_comment'
    model = Comment
    template_name = 'CommDel.html'
    success_url = 'http://127.0.0.1:8000/messages/comm'
    context_object_name = 'CommDel'


class CommConfirm(PermissionRequiredMixin, UpdateView):
    permission_required = 'newsportal.change_comment'
    model = Comment
    template_name = 'CommConfirm.html'
    form_class = CommConfirmForm
    success_url = 'http://127.0.0.1:8000/messages/comm'
