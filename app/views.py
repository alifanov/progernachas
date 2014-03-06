# Create your views here.
from django.http import HttpResponse
from app.models import Subscriber

def order(request):
    if request.POST.get('email') and request.POST.get('name'):
        Subscriber.objects.create(
            name=request.POST['name'],
            email=request.POST['email']
        )
    return HttpResponse('OK')
