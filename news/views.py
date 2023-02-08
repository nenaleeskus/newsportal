from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from .forms import PostForm
from .models import Post, Author
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = 'date'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        if 'news' in self.request.path.split('/'):
            queryset = Post.objects.order_by('-date').filter(type_choice='NW')
        else:
            queryset = Post.objects.order_by('-date').filter(type_choice='AR')
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class PostDetail(DetailView):
    model = Post
    template_name = 'news1.html'
    context_object_name = 'news1'

    def get_queryset(self):
        id_post = self.request.path.split('/')[-1]
        if 'news' in self.request.path.split('/'):
            queryset = Post.objects.order_by('-date').filter(type_choice='NW', id=id_post)
        else:
            queryset = Post.objects.order_by('-date').filter(type_choice='AR', id=id_post)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class PostSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news_search'

    def get_queryset(self):
        queryset = Post.objects.order_by('-date').filter(type_choice='NW')
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(user_id=4)
        if 'news' in self.request.path.split('/'):
            post.type_choice = 'NW'
            self.success_url = reverse_lazy('news_list')
        else:
            post.type_choice = 'AR'
            self.success_url = reverse_lazy('articles_list')
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_queryset(self):
        id_post = self.request.path.split('/')[-3]
        if 'news' in self.request.path.split('/'):
            queryset = Post.objects.order_by('-date').filter(type_choice='NW', id=id_post)
        else:
            queryset = Post.objects.order_by('-date').filter(type_choice='AR', id=id_post)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def form_valid(self, form):
        if 'news' in self.request.path.split('/'):
            self.success_url = reverse_lazy('news_list')
        else:
            self.success_url = reverse_lazy('articles_list')
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def form_valid(self, form):
        if 'news' in self.request.path.split('/'):
            self.success_url = reverse_lazy('news_list')
        else:
            self.success_url = reverse_lazy('articles_list')
        return super().form_valid(form)

    def get_queryset(self):
        # Получаем обычный запрос
        post_id = self.request.path.split('/')[-3]
        if 'news' in self.request.path.split('/'):
            queryset = Post.objects.order_by('-date').filter(type_choice='NW', id=post_id)
        else:
            queryset = Post.objects.order_by('-date').filter(type_choice='AR', id=post_id)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
