from django.shortcuts import render

# Create your views here.
def game_platform(request):
    return render(request, 'third_task/platform.html')

def game(request):
    games = {'first': 'Atomic Heart', 'second': 'Cyberpunk 2077', 'third': 'PayDay 2'}
    return render(request, 'third_task/games.html', context=games)

def cart(request):
    return render(request, 'third_task/cart.html')
