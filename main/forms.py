from django.forms import ModelForm, TextInput, Textarea, Select, URLInput
from main.models import Experience, Education


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience

        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Experience",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Gambar",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: BEM Fasilkom UI",
                    "maxlength": 255,
                }
            ),

            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu",
                    "rows": 3,
                }
            ),

            "category": Select(),

            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "major",
            "year",
            "description",
        ]

        labels = {
            "institution": "Nama Institusi",
            "major": "Jurusan",
            "year": "Tahun",
            "description": "Deskripsi",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Contoh: Universitas Indonesia",
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "Contoh: Sistem Informasi",
                }
            ),
            "year": TextInput(
                attrs={
                    "placeholder": "Contoh: 2025",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi pendidikan",
                    "rows": 3,
                }
            ),
        }