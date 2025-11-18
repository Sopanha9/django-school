from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    A = 2
    b = 3
    c = A + b
    return HttpResponse(f"The sum of {A} and {b} is {c}")

    
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")


# def say_hello(request, name, age):
#         return HttpResponse(f'Welcome to {name} and {age}')

#define route use keyword arguments
def introduce(request, name, age):
    return HttpResponse(f'My name is {name} and I am {age} years old.')

