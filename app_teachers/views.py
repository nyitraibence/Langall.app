from django.shortcuts import render

def start_teaching(request):
    return render(request, 'app_teachers/start_teaching.html')

def teachers(request):
    return render(request, 'app_teachers/teachers.html')