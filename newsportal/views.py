from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter, CommFilter
from .forms import PostForm, CommForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'newsportal/index.html'
    context_object_name = 'newsportal'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'newsportal/detailes.html'
    context_object_name = 'newsportal'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = Comment()
        return context



class PostCreate( PermissionRequiredMixin, CreateView ):
    permission_required = ('newsportal.add_post')
    form_class = PostForm
    model = Post
    template_name = 'Post_edit.html'

class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'Post_edit.html'

class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'Post_delete.html'
    success_url = reverse_lazy('post_list')

class CommentList(ListView):
    model = Comment
    template_name = 'CommentList.html'
    context_object_name = 'CommentList'
    ordering = '-dateComm'
    # paginate_by = 10

    def get_queryset(self):
        queryset = Comment.objects.filter(message__author__id=self.request.user.id)
        self.filterset = CommFilter(self.request.GET, queryset, request=self.request.user.id)
        if not self.request.GET:
            return Comment.objects.none()
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        context['get'] = self.request.GET
        return context


class CommCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommForm
    raise_exception = True
    template_name = 'CommCreate.html'

    def form_valid(self, form, *args, **kwargs):
        self.post = form.save(commit=False)
        self.post.author = self.request.user
        self.post.save()
        return super().form_valid(form)
