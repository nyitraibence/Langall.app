from django.shortcuts import render, redirect
from .models import Lesson
from core.models import CustomUser
from django.http import JsonResponse

def accept_lesson(request):
    lesson_id = request.GET.get('lesson_id', None)
    print('------------------------------')
    print("VERIFIED lesson (ID->",lesson_id,")")
    print('------------------------------')
    actual_lesson = Lesson.objects.get(pk=lesson_id)
    actual_lesson.is_verified = True
    actual_lesson.save()
    data = {'message' : "Elfogadva!"}
    return JsonResponse(data)

def reject_lesson(request):
    lesson_id = request.GET.get('lesson_id', None)
    print('------------------------------')
    print("REJECTED lesson (ID->",lesson_id,")")
    print('------------------------------')
    actual_lesson = Lesson.objects.get(pk=lesson_id)
    actual_lesson.is_rejected = True
    actual_lesson.save()
    data = {'message' : "Tanóra elutasítva!"}
    return JsonResponse(data)


def manage_fav(request):
    teacher_id = request.GET.get('teacher_to_manage', None)
    selected_teacher = CustomUser.objects.get(pk=teacher_id)

    manage_action = request.GET.get('manage_action', None)
    current_user = request.user

    if(manage_action == "fav"):
        selected_teacher.reverse_favourites.remove(current_user)
        selected_teacher.save()
        data = {'message' : "Eltávolítva a kedvencek közül!"}
    elif(manage_action == "not-fav-yet"):
        selected_teacher.reverse_favourites.add(current_user)
        selected_teacher.save()
        data = {'message' : "Felvéve kedvencek közé!"}

    return JsonResponse(data)