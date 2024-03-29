from django.shortcuts import render
from SocialTravel.models import Post, Futbol, Escuela
from SocialTravel.forms import PostForm, FutbolForm , EscuelaForm

def index(request):
    return render(request, "SocialTravel/index.html")


def mostrar_posts(request):
    context = {
         "posts": Post.objects.all(),
         "form": PostForm(),
         }

    
    return render(request, "SocialTravel/admin_post.html", context)


def agregar_post(request):
    post_form = PostForm(request.POST)
    post_form.save()
    context = {
         "posts": Post.objects.all(),
         "form": PostForm(),
         }

    return render(request, "SocialTravel/admin_post.html", context)


def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = { "posts": Post.objects.filter(carousel_caption_title__icontains=criterio).all()}
    return render(request, "SocialTravel/admin_post.html", context)




def mostrar_futbol(request):
    context = {
         "futbol": Futbol.objects.all(),
         "form": FutbolForm(),
         }

    
    return render(request, "SocialTravel/admin_futbol.html", context)


def agregar_futbol(request):
    futbol_form = FutbolForm(request.POST)
    futbol_form.save()
    context = {
         "futbol": Futbol.objects.all(),
         "form": FutbolForm(),
         }

    return render(request, "SocialTravel/admin_futbol.html", context)


def buscar_futbol(request):
    criterio = request.GET.get("criterio")
    context = { "futbol": Futbol.objects.filter(carousel_caption_title__icontains=criterio).all()}
    return render(request, "SocialTravel/admin_futbol.html", context)







def mostrar_escuela(request):
    context = {
         "escuela": Escuela.objects.all(),
         "form": EscuelaForm(), 
         }

    
    return render(request, "SocialTravel/admin_escuela.html", context)


def agregar_escuela(request):
    escuela_form = EscuelaForm(request.POST)
    escuela_form.save()
    context = {
         "escuela": Escuela.objects.all(),
         "form": EscuelaForm(),
         }

    return render(request, "SocialTravel/admin_futbol.html", context)


def buscar_escuela(request):
    criterio = request.GET.get("criterio")
    context = { "futbol": Escuela.objects.filter(carousel_caption_title__icontains=criterio).all()}
    return render(request, "SocialTravel/admin_escuela.html", context)