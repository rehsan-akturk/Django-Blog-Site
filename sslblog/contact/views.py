from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse 

from contact.forms import ContactForm 
from django.core.mail import send_mail
# Create your views here.


def contact_us(request):

    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['akturkrehsan@gmail.com'])
            return HttpResponse('MEsajınız bize ulaştı!')
    else:
        form=ContactForm()
    
    return render(request,'../Templates/contact.html',{'form':form})

