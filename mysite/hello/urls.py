from django.urls import path
from .views import  greet, hello_world,introduce
# . meaning current directory

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('greet/<str:name>/', greet, name='greet'),
    path('introduce/', introduce, name='say_hello', kwargs={'name':'Panha', 'age':22}),
]