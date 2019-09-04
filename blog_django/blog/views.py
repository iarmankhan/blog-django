from django.shortcuts import render

posts = [
    {
        'author': 'Arman',
        'title': 'test1',
        'content': 'First post',
        'date_posted': 'sdd'
    },
    {
        'author': 'ArmanKhn',
        'title': 'test2',
        'content': 'Second post',
        'date_posted': 'sdd'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})