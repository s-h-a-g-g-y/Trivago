from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel
from django.db.models import Q

def index(request):
    return render(request, 'hotel/base.html')

# Create your views here.
def search(request):
    if request.method=='POST':
        value = request.POST['search_value']
        if value:
            match = Hotel.objects.filter(Q(name__icontains=value) |
                                        Q(city__icontains=value)
                                        )
            if match:
                args = {'names':match}
                return render(request,'hotel/detail.html', args)
            else:
                return render(request,'hotel/fail.html')
        else:
            return render(request,'hotel/base.html')

    return render(request,'hotel/base.html')
