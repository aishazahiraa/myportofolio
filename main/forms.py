from django.forms import ModelForm, TextInput, Textarea, Select, URLInput
from main.models import Experience


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