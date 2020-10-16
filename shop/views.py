from django.shortcuts import render

from django.http import HttpResponse
from shop.models import Game

# Create your views here.
def index(request):
 if request.method == 'ET':
  return HttpResponse('Hello')

def get_games(request):
 if request.method == 'GET':
  game = Game.objects.all()[0]
  return HttpResponse(str(game.title) + ' $' + str(game.price))

def get_html(request):
 games = ['Tekken', 'GTA', 'Spider Man']
 if request.method == "GET":
  return render(request, 'login.html', {'games': games})
