from django.shortcuts import render

from django.http import HttpResponse

def index(request):
        #return HttpResponse("<h1>viva peron</h1>")
        return render(request, 'templatebychorga/index.html', {})