from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import render
import os
# Create your views here.

""" def home(request):
    #return HttpResponse('<h1>Califica tu servici</h1>')
   return render(request, 'home.html', {'name':'Gabriela'}) """

def home(request):
    return render(request, "home.html")

def perfil(request):
    file_path = os.path.join(os.path.dirname(__file__), "usados.json")  # ✅ Fixed path

    try:
        with open(file_path, encoding="utf-8") as json_file:
            purchases = json.load(json_file)
            print("✅ Loaded purchases:", purchases)  # Debugging output
    except FileNotFoundError:
        print("❌ Error: JSON file not found at", file_path)
        purchases = []
    except json.JSONDecodeError:
        print("❌ Error: JSON file is not formatted correctly")
        purchases = []

    return render(request, "perfil.html", {"purchases": purchases})


