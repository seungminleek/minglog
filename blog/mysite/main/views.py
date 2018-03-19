from django.shortcuts import render
from post.models import Post

# Create your views here.
def mains(request):
    context = {}
    context["posts11"] = Post.objects.all()
    return render(request, "main.html", context)
