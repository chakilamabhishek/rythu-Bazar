from rythubazarapp.models import *
import django.forms as forms


class AddCrop(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCrop, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })
    class Meta:
        model = farmer
        exclude=['farmername',]
