from django.shortcuts import render, redirect
from .forms import PostForm


# Create your views here.
def post_new(request):
    context={}

    if request.method =="POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()

            return redirect('de', pk=post.pk)
    else:
        context['form'] = PostForm()

    return render(request,'new.html', context)