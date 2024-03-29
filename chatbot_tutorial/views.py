from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render

from chatbot_tutorial.models import User


def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    #  message['text'] == name
    us=User.objects.create(name=message['text'])
    print((us.id))
    result_message = {
        'type': 'text'
    }
    result_message['userid']=us.id
    result_message['text'] = "Hello "+us.name+"! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    
    return result_message
    

def respond_to_websocketsButton(message):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'fat' in message['text']:
        u=User.objects.get(id=message['userid'])
        u.fat+=1
        u.save()
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message['text']:
        u=User.objects.get(id=message['userid'])
        u.stupid+=1
        u.save()
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message['text']:
        u=User.objects.get(id=message['userid'])
        u.dumb+=1
        u.save()
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message
    
def botreport(request):
    context={}
    context['table']=User.objects.all()
    return render(request, 'chatbot_tutorial/table.html', context)

def index(request):
    return render(request, 'chatbot_tutorial/index.html')
