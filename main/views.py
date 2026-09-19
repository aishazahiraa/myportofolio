from django.shortcuts import render, redirect
from main.models import Experience
from .models import Hobby, Education, FunFact
from main.forms import ExperienceForm, EducationForm
from django.core import serializers
from django.http import HttpResponse

def show_main(request):
    context = {
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
        "experience_list": Experience.objects.all(),
    }

    return render(request, "experience.html", context)

def more_about_me(request):
    hobbies = Hobby.objects.all()
    educations = Education.objects.all()
    funfacts = FunFact.objects.all()

    context = {
        'hobbies': hobbies,
        'educations': educations,
        'funfacts': funfacts,
    }

    return render(request, 'more_about_me.html', context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")

    context = {
        "name": "Aisha Ibnaty Zahira",
        "form": form,
    }

    return render(request, "experience_form.html", context)

def show_json(request):
    data = Experience.objects.all()

    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def show_json_by_id(request, id):
    data = Experience.objects.filter(pk=id)

    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def show_xml(request):
    data = Experience.objects.all()

    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

def show_xml_by_id(request, id):
    data = Experience.objects.filter(pk=id)

    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:more_about_me")

    context = {
        "form": form,
    }

    return render(request, "education_form.html", context)

def update_education(request, id):
    education = Education.objects.get(pk=id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:more_about_me")

    context = {
        "form": form,
    }

    return render(request, "education_form.html", context)

def delete_education(request, id):
    education = Education.objects.get(pk=id)
    education.delete()

    return redirect("main:more_about_me")
