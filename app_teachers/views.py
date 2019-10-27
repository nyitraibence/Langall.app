from django.shortcuts import render
from core.models import CustomUser
from .forms import TeacherForm

def start_teaching(request):
    teacher_form = TeacherForm
    return render(request, 'app_teachers/start_teaching.html', {'form' : teacher_form})

def teachers(request):
    teachers = CustomUser.objects.filter(is_teacher=True)
    return render(request, 'app_teachers/teachers.html', {'teachers' : teachers})