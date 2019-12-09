from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy

def index(request):
    return render(request, 'blog/index.html')

index = ListView.as_view(model=Post, template_name='blog/index.html')
post_new = CreateView.as_view(model=Post, fields="__all__")
post_detail = DetailView.as_view(model=Post)
post_edit = UpdateView.as_view(model=Post, fields='__all__')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

class CommentCreatView(CreateView):
    model = Comment
    fields = ['message']

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk']) #kwargs는 url인자
        super().form_valid(form)

    def get_absolute_url(self):
        self.object



