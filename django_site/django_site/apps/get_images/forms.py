from .models import PagesToScan
from django.forms import ModelForm


class PagesToScanForm(ModelForm):
    class Meta:
        model = PagesToScan
        fields = ['url']
        labels = {
            'url': '',
        }
