from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Users, Item

class Home(TemplateView):
    template_name = 'base.html'

def dashboard(request):
    Item = Item.objects.all()
    return render(request, 'dashboard.html', {'Item': Item})
    #return render (request,'dashboard.html')

def signup(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            x = Users()
            x.email = request.POST.get('email')
            if not Users.objects.filter(email=x.email).exists():
                print ('new')
                x.save()
            else:
                render(request, 'dashboard.html')
        return render(request, 'dashboard.html')
    return render(request, 'signup.html')

#@login_required
def additem(request):
    if request.method == 'POST':
        if request.POST.get('prod_name') and request.POST.get('prod_description') and request.POST.get(
                'min_bid_price') and request.POST.get('end_date_time'):
            x = Item()
            x.prod_name = request.POST.get('prod_name')
            x.prod_description = request.POST.get('prod_description')
            x.min_bid_price = request.POST.get('min_bid_price')
            x.end_date_time = request.POST.get('end_date_time')
            x.save()
    else:
        render(request, 'dashboard.html')

    return render(request, 'additem.html')

