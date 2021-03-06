from django.shortcuts import render, redirect
from core.models import CustomUser
from .models import TeacherProfile, Lesson, TimeCell
from social_django.models import UserSocialAuth
from .forms import TeacherForm, PingTeacherForm


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
    top_3_appointments = Lesson.objects.filter(host_teacher=request.user.id, is_verified=True, is_over=False).order_by('start_time')[:3]
    unverified_appointments = Lesson.objects.filter(host_teacher=request.user.id, is_verified=False, is_rejected=False).order_by('-created')
    passed_3_appointments = Lesson.objects.filter(host_teacher=request.user.id, is_verified=True, is_over=True).order_by('-start_time')[:3]
    
    content = {
        'top_3': top_3_appointments,
        'new_requests': unverified_appointments,
        'past_3': passed_3_appointments
    }

    content["days"]=["H","K","Sze","Cs","P","Szo","V"]
    content["hours"] =[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    content["teacher_time_cells"] = request.user.time_cell.all()

    return render(request, 'app_teachers/teacher_panel.html', content)



def teachers(request):
    teachers = CustomUser.objects.filter(is_teacher=True).order_by('-teacherprofile__form_fill_factor')
    return render(request, 'app_teachers/teachers.html', {'teachers' : teachers})







def single_teacher(request, pk):
    the_teacher = CustomUser.objects.get(id = pk)
    content = {
        'teacher' : the_teacher
    }

    content["days"]=["H","K","Sze","Cs","P","Szo","V"]
    content["hours"] =[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    content["teacher_time_cells"] = the_teacher.time_cell.all()

    if request.method == "POST":
        form = PingTeacherForm(request.POST)
        if form.is_valid():
            ping_message = form.save(commit=False)
            ping_message.host_teacher = the_teacher
            ping_message.student = request.user
            ping_message.save()
            return redirect('single_teacher', pk=the_teacher.pk)
    else:
        form = PingTeacherForm()
    content['form'] = form
    return render(request, 'app_teachers/single_teacher.html', content)






def single_lesson(request, pk):
    the_lesson = Lesson.objects.get(id = pk)
    return render(request, 'app_teachers/single_lesson.html', {'lesson' : the_lesson})



def favourites(request):
    current_user = request.user
    favourites = CustomUser.objects.filter(reverse_favourites=current_user)
    return render(request, 'app_teachers/favourites.html', {'favourites' : favourites})