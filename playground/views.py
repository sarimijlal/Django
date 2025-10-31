from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def hello(request):
    # return render(request, "hello.html", {'name': 'sarim'})
    return HttpResponse("Hello, sarim!")

def sqlquery(request):
    queryset = Product.objects.all()

    for query in queryset:
        print(query)

    return HttpResponse('done')