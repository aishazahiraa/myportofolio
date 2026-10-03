from django.shortcuts import render, redirect, get_object_or_404
from main.models import Experience
from .models import Hobby, Education, FunFact
from main.forms import ExperienceForm, EducationForm
from django.core import serializers
import json
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Aisha Ibnaty Zahira",
        "form": form,
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        response = redirect("main:show_main")
        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        return response

    context = {
        "name": "Aisha Ibnaty Zahira",
        "form": form,
    }

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie("last_login")
    return response

def show_main(request):
    last_login = request.COOKIES.get(
    "last_login",
    "Belum ada sesi login / Cookie tidak ditemukan"
)
    context = {
        "last_login": last_login,
        "name": "Aisha Ibnaty Zahira",
        "npm": "2506624726",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer "
            "Universitas Indonesia."
        ),
    }

    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Aisha Ibnaty Zahira",
    }

    return render(request, "experience.html", context)

def get_experiences_json(request):
    experiences = Experience.objects.prefetch_related("starred_by").all()

    data = []

    for experience in experiences:
        starred_users = experience.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        starred_by_names = ", ".join(
            [user.username for user in starred_users]
        )

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.get_category_display(),
                "thumbnail": experience.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def more_about_me(request):
    hobbies = Hobby.objects.all()
    educations = Education.objects.all()
    funfacts = FunFact.objects.all()

    is_editor = (
    request.user.is_authenticated
    and request.user.groups.filter(name="Editor").exists()
)

    context = {
        'hobbies': hobbies,
        'educations': educations,
        'funfacts': funfacts,
        "is_editor": is_editor,
    }

    return render(request, 'more_about_me.html', context)

@login_required(login_url="/login/")
@require_POST
def create_experience(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"success": False, "message": "Anda tidak memiliki izin untuk menambahkan experience."},
            status=403
        )

    form = ExperienceForm(request.POST)

    if form.is_valid():
        experience = form.save()

        return JsonResponse(
            {
                "success": True,
                "message": "Experience berhasil ditambahkan.",
                "id": str(experience.id),
            },
            status=201
        )

    return JsonResponse(
        {
            "success": False,
            "message": "Data yang dimasukkan tidak valid.",
            "errors": form.errors,
        },
        status=400
    )

def show_json(request):
    data = Education.objects.all()

    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def show_json_by_id(request, id):
    data = Education.objects.filter(pk=id)

    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def show_xml(request):
    data = Education.objects.all()

    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

def show_xml_by_id(request, id):
    data = Education.objects.filter(pk=id)

    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

@login_required
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:more_about_me")

    context = {
        "form": form,
    }

    return render(request, "education_form.html", context)

@login_required
def update_education(request, id):
    is_editor = request.user.groups.filter(name="Editor").exists()

    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied

    education = Education.objects.get(pk=id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:more_about_me")

    context = {
        "form": form,
    }

    return render(request, "education_form.html", context)

@login_required
def delete_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = Education.objects.get(pk=id)
    education.delete()

    return redirect("main:more_about_me")

def show_education_from_json(request):
    json_data = serializers.serialize("json", Education.objects.all())
    data = json.loads(json_data)

    context = {
        "educations": data,
    }

    return render(request, "education_json.html", context)

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.user in experience.starred_by.all():
        experience.starred_by.remove(request.user)
        is_starred = False
    else:
        experience.starred_by.add(request.user)
        is_starred = True

    return JsonResponse({
        "is_starred": is_starred,
        "star_count": experience.starred_by.count(),
    })