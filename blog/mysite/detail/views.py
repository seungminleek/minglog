from django.shortcuts import render, get_object_or_404
from post.models import Post

# Create your views here.
def post_detail(request, pk):
    context={}
    context["post"] = get_object_or_404(Post, pk=pk)


    return render(request, "detail.html", context)