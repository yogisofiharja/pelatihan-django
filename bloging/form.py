from django.forms import ModelForm
from bloging.models import Artikel
class FormArtikel(ModelForm):

    class Meta:
        model = Artikel
