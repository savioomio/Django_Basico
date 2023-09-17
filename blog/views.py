# from django.shortcuts import render
from django.shortcuts import render
from blog.data import posts

def blog(request):
    context = {
        'text_blog': 'Estamos no meu blog',
        'ola_blog': 'Bem vindo,',
    }
    return render(
        request, 
        'blog/index.html',
        context,
    )

def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    context = {
        'text_post': 'Esse é o post:',
        'id_post': post_id,
        'post_title': post['title'],
        'post_body': post['body'],
        'post': [found_post],
    }

    return render(
        request, 
        'blog/post.html',
        context,
    )

def exemplo(request):
    context = {
        'exemplo': 'um exemplo de blog',
        'posts': posts
    }
    return render(
        request, 
        'blog/exemplo.html',
        context,
    )