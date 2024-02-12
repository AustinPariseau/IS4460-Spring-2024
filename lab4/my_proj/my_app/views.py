from django.views import View
from django.shortcuts import render, redirect
from . import my_functions
from . import my_objects

def fix_name(name: str):
    new_name = name.title()
    return new_name.lower




class HomePageView(View):
    def get(self, request):
        orig_name = "aUSTIN"
        name = fix_name(orig_name) 

        names = ['John', 'Luke', 'Phil']
        fixed_names = my_functions.fix_names_list(names)

        car1 = my_objects.Car(make="Honda", model="Civic", year=2020, color="blue", sound="hond honk")
        car2 = my_objects.Car(make="Jeep", model="Wrangler", year=2008, color="red", sound="beep beep")
        motorcycle1 = my_objects.Motorcycle(make="Harley-Davidson", model="Street Glide", year=2019, color="black", sound="vroom vroom")

        context = {
            'hi': 'help! I dont know what im doing',
            'name': name,
            'orig_name': orig_name,
            'names': names,
            'fixed_names': fixed_names,
            'car1': car1,
            'car2': car2,
            'motorcycle1': motorcycle1
        }
        return render(request, 'my_app/index.html', context)
