from django.shortcuts import render
import json
import urllib.request
from django.core.mail import send_mail


# Create your views here.
def index(request):
    res=urllib.request.urlopen('https://www.boredapi.com/api/activity')
    jsondata =json.load(res)
    return render(request,'index.html',{"joke":jsondata})

def email (request):
    
    send_mail( 
        "to my lovely friend",
        " you seem to be bored how about you give a try at the activity am advising you :",
        "wilsonmwaura697@gmail.com",
        ["wilsonmwaura697@dmail.com"],
    )

