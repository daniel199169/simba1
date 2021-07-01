from django.template.loader import get_template, render_to_string
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from django.conf import settings

# Create your views here.


def home(request):
    """
        this view displays the mains SWMS Dashboard
        features:
            button to create new SWMS
            list of current SWMS and buttons to Update, Print to PDF, and Delete
    """

    swms = Swms.objects.all()

    context = {
        'swms': swms,
    }

    return render(request, 'dashboard.html', context)


def create_swms(request):
    """
        this view starts the swms form creation.
        the user selects which SWMS groups are to be included in the SWMS form (section 3)
        features:
            radio buttons to select which SWMS Groups to add to form. There will be 40+.
    """
    swms_groups = SwmsGroupDefault.objects.all()

    context = {
        'swms_groups': swms_groups,
    }

    if request.method == 'POST':
        request.session['swms_groups'] = request.POST.getlist('swmsgroup_ids')
        return redirect('swms_form')

    return render(request, 'create_swms.html', context)


def update_swms(request, pk):
    """
        this view starts the swms form creation.
        the user selects which SWMS groups are to be included in the SWMS form
        features:
            radio buttons to select which SWMS Groups to add to form. There will be 40+.
    """
    swms = Swms.objects.get(id=pk)
    swms_form = SwmsForm(instance=swms)

    context = {
        'swm_form': swms_form
    }

    if request.method == 'POST':
        form = SwmsForm(request.POST)

        if form.is_valid():
            print("Valid Form")
            form.save()

            return render(request, 'swms_form/swms_form.html', {'swm_form': form})
        else:
            print("Invalid Form")
            print(form.errors)

            return render(request, 'swms_form/swms_form.html', {'swm_form': form})

    return render(request, 'swms_form/swms_form.html', context)


def delete_swms(request):
    """
        this view starts the swms form creation.
        the user selects which SWMS groups are to be included in the SWMS form
        features:
            radio buttons to select which SWMS Groups to add to form. There will be 40+.
    """
    return render(request, 'dashboard.html')


def swms_form(request):
    """
        this view starts the swms form creation.
        the user selects which SWMS groups are to be included in the SWMS form
        features:
            radio buttons to select which SWMS Groups to add to form. There will be 40+.
    """

    if 'swms_groups' in request.session:
        swms_group_ids = request.session['swms_groups']
        swms_groups = SwmsGroupDefault.objects.filter(id__in=swms_group_ids)
    else:
        return HttpResponseBadRequest

    if request.method == 'POST':
        form = SwmsForm(request.POST)
        form.swms_groups = swms_group_ids
        if form.is_valid():
            print("Valid Form")
            form.save()
            return render(request, 'dashboard.html')
        else:
            print("Invalid Form")
            print(form.errors)
            return render(request, 'swms_form/swms_form.html', {'swm_form': form})

    swms_form = SwmsForm(auto_id=True)

    context = {
        'swms_groups': swms_groups,
        'swm_form': swms_form,
    }

    return render(request, 'swms_form/swms_form.html', context)


def print_swms(request, pk):
    """
        this view should print the selected SWMS form to PDF
    """

    swms = Swms.objects.get(id=pk)
    swms_form = SwmsForm(instance=swms)

    context = {
        'swm_form': swms_form
    }

    return render(request, 'dashboard.html', context)