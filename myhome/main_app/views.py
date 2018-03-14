from django.shortcuts import render
from .models import MessageModel

def home(request):
    return render(request, 'onepage.html')


def contact(request):
    if request.method == 'POST':
        message = MessageModel(
            name=request.POST.get('name'),
            telephone=request.POST.get('telephone'),
            email=request.POST.get('email'),
            qq=request.POST.get('qq/wechat'),
            content=request.POST.get('message'),
        )
        message.save()
    return render(request, 'onepage.html')

