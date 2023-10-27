from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.
def home(request):
    if request.method == "POST":
        name_of_food = request.POST['food_consumed']

        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(name_of_food)
        response = requests.get(api_url, headers={'X-Api-Key': 'qJXdAxQG9UWoM2g1bHQ/Cw==ODvpMi16dBa2hv7I'})
    
        json_data = response.json()
        context = {'json_data':json_data}
    else:
        context = ''
    return render(request, 'index.html', context)



def delete(request, id):
    consumed = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed.delete()
        return redirect('home')
        cons = Consume.objects.filter(food_consumed=consumed)
    else:
        cons = Consume.objects.all()
    return render(request, 'delete.html', {'cons':cons})
