from django.shortcuts import render
#incluir o mdelo que temos em models.py

from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
            form = PostForm(request.POST, instance=post)

        return render(request, 'blog/post_edit.html', {'form': form})
