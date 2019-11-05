from django.shortcuts import render
from core.models import CustomUser
from .models import TeacherProfile
from social_django.models import UserSocialAuth
from .forms import TeacherForm


def start_teaching(request):
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            new_teacher = teacher_form.save(commit=False)
            new_teacher.user = request.user
            new_teacher.save()

            request.user.is_teacher = True
            request.user.save()

            teacher_form = TeacherForm()
            return redirect('homepage')
    else:
        teacher_form = TeacherForm()
        return render(request, 'app_teachers/start_teaching.html', {'form' : teacher_form})




def teacher_panel(request):
    return render(request, 'app_teachers/teacher_panel.html')



def teachers(request):
    teachers = CustomUser.objects.filter(is_teacher=True)
    return render(request, 'app_teachers/teachers.html', {'teachers' : teachers})