import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, Consume

# Create your views here.

# getting data from API Ninja and saving it in a database
def home(request):
    if request.method == "POST":
        name_of_food = request.POST['food_consumed']

        try:
            api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(name_of_food)
            response = requests.get(api_url, headers={'X-Api-Key': 'qJXdAxQG9UWoM2g1bHQ/Cw==ODvpMi16dBa2hv7I'})
            json_data = response.json()

            create_food_data = Food.objects.create(
                food_name=name_of_food,  carbs=json_data[0]['carbohydrates_total_g'],
                protein=json_data[0]['protein_g'],  fats=json_data[0]['fat_total_g'],
                calories=json_data[0]['calories']
            )
        except IndexError or ConnectionError:
            return errors(request)

        cons = Food.objects.get(food_name=name_of_food)
        return redirect('home')

    else:
        cons = Food.objects.all()
    context = {'cons':cons}

    return render(request, 'index.html', context)


# function to delete a food item from the selected foods
def delete(request, name):
    consumed = Food.objects.get(food_name=name)

    if request.method == 'POST':
        consumed.delete()
        return redirect('home')

    context = {'consumed':consumed}
    return render(request, 'delete.html', context)              


def errors(request):
    return render(request, 'errors.html')