from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def add_post(request:HttpRequest):

    if request.method == "POST":
        #addin a new post in database
        new_post = Post(title=request.POST["title"], description=request.POST["description"], release_date=request.POST["release_date"], is_published=request.POST["is_published"])
        new_post.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_post.html")



def index_page(request:HttpRequest):
    

    post = Post.objects.all()

    return render(request, "main_app/index.html", {"post" : post})


def game_detail(request:HttpRequest, game_id):

    game = Game.objects.get(id=game_id)

    return render(request, 'main_app/game_detail.html', {"game" : game})


def update_game(request:HttpRequest, game_id):

    game = Game.objects.get(id=game_id)
    iso_date = game.release_date.isoformat()

    #updating the game
    if request.method == "POST":
        game.title = request.POST["title"]
        game.description = request.POST["description"]
        game.rating = request.POST["rating"]
        game.release_date = request.POST["release_date"]
        game.is_published = request.POST["is_published"]
        game.save()

        return redirect("main_app:game_detail", game_id=game.id)

    return render(request, 'main_app/update_game.html', {"game" : game, "iso_date" : iso_date})



def delete_game(request:HttpRequest, game_id):
    
    game = Game.objects.get(id=game_id)
    game.delete()

    return redirect("main_app:index_page")


def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    Post = Post.objects.filter(title__contains=search_phrase,)

    return render(request, "main_app/search_page.html", {"post" : post})