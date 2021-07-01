from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from Webcheckfuel.apps.parsing.models import Train

from .main import startgetinf as get


@login_required
def index(request):
    if request.user.is_authenticated:
        messages = Train.objects.all()
        sum_all_vag = Train.objects.aggregate(Sum("vag_all"))["vag_all__sum"]
        sum_vag_h = Train.objects.aggregate(Sum("vag_h"))["vag_h__sum"]
        sum_vag_l = Train.objects.aggregate(Sum("vag_l"))["vag_l__sum"]
        result = sum_vag_h + sum_vag_l
        context = {
            "messages": messages,
            "sum_all_vag": sum_all_vag,
            "sum_vag_h": sum_vag_h,
            "sum_vag_l": sum_vag_l,
            "result": result,
        }
        return render(request, "parsing/index.html", context)
