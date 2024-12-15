from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def game_platform(request):
    return render(request, 'fourth_task/platform.html')

def game(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {'game_dict': game_dict}
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')

def base(request):
    return render(request, 'fourth_task/base.html')



