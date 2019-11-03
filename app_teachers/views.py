from django.shortcuts import render
from core.models import CustomUser
from social_django.models import UserSocialAuth
from .forms import TeacherForm

def start_teaching(request):
    teacher_form = TeacherForm
    return render(request, 'app_teachers/start_teaching.html', {'form' : teacher_form})

def teachers(request):
    teachers = CustomUser.objects.filter(is_teacher=True)
    # test_teachers = CustomUser.objects.filter(email='nyitrai.bence96@freemail.hu')
    # # users_extra_data = UserSocialAuth.objects.all()
    # for item in test_teachers:
    #     print('-------------------')
    #     print(type(item.social_auth))
    #     print('-------------------')
    #     print(item.social_auth)
    #     # print('-------------------')
    #     # print(item.social_auth.extra_data['profile_url'])
    print('-------------------')
    return render(request, 'app_teachers/teachers.html', {'teachers' : teachers})