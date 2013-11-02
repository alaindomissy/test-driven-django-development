from django.views.generic import ListView

from blog.models import BlogPost


class HomeView(ListView):
    template_name = 'index.html'
    queryset = BlogPost.objects.order_by('-created_at')

home = HomeView.as_view()
