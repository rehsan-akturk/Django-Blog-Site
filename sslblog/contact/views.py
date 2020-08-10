from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.contrib import messages

from contact.forms import ContactForm 
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def contact_us(request):

    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message =form.cleaned_data['message']
            send_mail(sender_name, message ,sender_email , ['akturkrehsan@gmail.com'])
            return HttpResponse('Mesajınız bize ulaştı!')
        return HttpResponseRedirect('/contact/thanks/')
           

        
    else:
        form=ContactForm()
    
    return render(request,'../Templates/contact.html',{'form':form})

