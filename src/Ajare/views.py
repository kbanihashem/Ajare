from django.shortcuts import render, redirect

"""
Don't add any functions in this app except the index page
"""


def index(request):
    return redirect("about_page")
#    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
