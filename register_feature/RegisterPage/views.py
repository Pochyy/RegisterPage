from django.shortcuts import render

def register_page(request):
    return render(request, "RegisterFrontEnd.html")

