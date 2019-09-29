from datetime import date

from .models import Document
from .forms import DocumentForm

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Amber
from .models import KCX
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AmberForm
from django .shortcuts import redirect
from django.contrib import messages

# Create your views here.





@login_required
def main_report(request):

    posts_1 = Amber.objects.order_by('-checked_date')
    posts_2=  KCX.objects.order_by('-checked_date')
    documents = Document.objects.all()

    object_list = list(chain(posts_1, posts_2))
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')

    try:
        posts =paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'quality_base/common/main_report.html', {'page':page, 'posts':posts, 'documents':documents})

@login_required
def detail_report (request,year,month,day):
    posts_1 = Amber.objects.filter(checked_date__year = year,
                                checked_date__month = month,
                                checked_date__day = day)

    posts_2 = KCX.objects.filter(checked_date__year = year,
                                checked_date__month = month,
                                checked_date__day = day)

    object_list = list(chain(posts_1, posts_2))
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return  render(request,'quality_base/common/detail_report.html',{'posts' : posts} )


@login_required
def controller_raport (request,year,month,day,person):
    posts_1 = Amber.objects.filter(checked_date__year=year,
                                 checked_date__month=month,
                                 checked_date__day=day,
                                 controller__username  = person
                                )
    posts_2 = KCX.objects.filter(checked_date__year=year,
                                   checked_date__month=month,
                                   checked_date__day=day,
                                   controller__username  = person
                                )


    object_list = list(chain(posts_1, posts_2))
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return  render(request,'quality_base/common/controller_report.html',{'posts' : posts} )

@login_required
def new_amber(request):
    documents = Document.objects.all()
    if request.method == "POST":
       form_1 = AmberForm(request.POST)
       form_2 = DocumentForm(request.POST, request.FILES)
       if form_1.is_valid():
            amber=form_1.save(commit=False)
            amber.controller = request.user
            amber.checked_date=timezone.now()
            amber.save()
            messages.success(request, 'Zapisano ostatni wpis')

       if  form_2.is_valid():
           form_2.save()
       return redirect('/',name='main_report')
    else:
        form_1=AmberForm()
        form_2=DocumentForm()
        return render (request,'quality_base/common/amber_edit.html',{'form_1':form_1,'form_2':form_2})
