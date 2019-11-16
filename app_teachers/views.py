from django.shortcuts import render
from core.models import CustomUser
from .models import TeacherProfile, Lesson
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
    top_3_appointments = Lesson.objects.filter(host_teacher=request.user.id).order_by('start_time')[:3]
    unverified_appointments = Lesson.objects.filter(host_teacher=request.user.id, is_verified=False).order_by('start_time')
    content = {
        'top_3': top_3_appointments,
        'new_requests': unverified_appointments
    }
    return render(request, 'app_teachers/teacher_panel.html', content)



def teachers(request):
    teachers = CustomUser.objects.filter(is_teacher=True)
    return render(request, 'app_teachers/teachers.html', {'teachers' : teachers})



def single_teacher(request, pk):
    the_teacher = CustomUser.objects.get(id = pk)
    print(type(the_teacher))
    return render(request, 'app_teachers/single_teacher.html', {'teacher' : the_teacher})