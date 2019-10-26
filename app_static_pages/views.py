from django.shortcuts import render

def about(request):
    return render(request, 'app_static_pages/about.html')

def exams(request):
    return render(request, 'app_static_pages/exams.html')
