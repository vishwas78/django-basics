from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView


from blog_app.forms import BlogForm


@login_required()
def BlogCreateView(request):
    print(request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return HttpResponse("Thank you for submitting the blog")
    else:
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blog_app/blog_input.html', context=context)
