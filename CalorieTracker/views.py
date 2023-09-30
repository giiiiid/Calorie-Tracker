from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.
def home(request):
    if request.method == "POST":

        name_of_food = request.POST['food_consumed']
        consume = Food.objects.get(food_name=name_of_food)
        cn = Consume(food_consumed=consume)
        cn.save()
        return redirect('home')
        foods = Food.objects.all()
        cons = Consume.objects.filter(food_consumed=consume)

    else:
        foods = Food.objects.all()
        cons = Consume.objects.all()

    return render(request, 'index.html', {'foods':foods, 'cons':cons})



def delete(request, id):
    consumed = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed.delete()
        return redirect('home')
        cons = Consume.objects.filter(food_consumed=consumed)
    else:
        cons = Consume.objects.all()
    return render(request, 'delete.html', {'cons':cons})
