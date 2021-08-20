from django import forms

from . import models as pars_models


class UploadedFileForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = pars_models.UploadedFile
        fields = ["file"]
