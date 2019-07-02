from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Check

# Create your views here.
def main_report(request):
    posts = Check.objects.all()
    return render(request, 'quality_base/common/main_report.html', {'posts': posts})

def detail_report (request,year,month,day):
    posts = Check.objects.filter(checked_date__year = year,
                                checked_date__month = month,
                                checked_date__day = day)

    return  render(request,'quality_base/common/detail_report.html',{'posts' : posts} )

def controller_raport (request,year,month,day,person):
    posts = Check.objects.filter(checked_date__year=year,
                                 checked_date__month=month,
                                 checked_date__day=day,
                                 controller__username  = person
                                )
    return  render(request,'quality_base/common/controller_report.html',{'posts' : posts} )