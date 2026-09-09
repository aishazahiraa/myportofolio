from django.shortcuts import render
from main.models import Experience

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