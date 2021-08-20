from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from apps.parsing.forms import UploadedFileForm
from apps.parsing.models import Train


@login_required
def index(request):
    if request.user.is_authenticated:
        messages = Train.objects.all()
        sum_all_vag = Train.objects.aggregate(Sum("vag_all"))["vag_all__sum"]
        sum_vag_h = Train.objects.aggregate(Sum("vag_h"))["vag_h__sum"]
        sum_vag_l = Train.objects.aggregate(Sum("vag_l"))["vag_l__sum"]
        result = sum_vag_h + sum_vag_l

        return render(request, "parsing/index.html", locals())


def upload(request):
    form_uploaded_files = UploadedFileForm()

    return render(request, "parsing/upload_file_form.html", locals())
