from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Component, ComponentCategory
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ComponentForm
from django.contrib import messages



# Create your views here.

#################################################################
#################   FETCHING COMPONENTS    ######################
#################################################################

@login_required
def ComponentListView(request):
    qs = Component.objects.filter(avialable = True)
    cat = ComponentCategory.objects.all()
    return render(request, 'components/components.html', {'qs':qs, 'cat':cat})

@login_required
def CatComponentListView(request, id):
    qs = Component.objects.filter(category__id__exact = id, avialable = True)
    cat = ComponentCategory.objects.all()
    return render(request, 'components/components.html', {'qs':qs, 'cat':cat})



#################################################################
###################    CRUD CATEGORY     ########################
#################################################################

@staff_member_required(login_url='accounts:auth-login')
def all_categories(request):
    cats = ComponentCategory.objects.all()
    return render(request, 'components/category_list.html', {'cats':cats})


@staff_member_required(login_url='accounts:auth-login')
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            messages.info(request, 'New category added')
            return redirect('components:all-categories')
        else:
            messages.info(request, 'form data invalid')            
    else:
        form = CategoryForm()

    return render(request, 'components/create_category.html')


@staff_member_required(login_url='accounts:auth-login')
def update_category(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(ComponentCategory, id = id)
        form = CategoryForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            messages.info(request,'category updated successfully')

            return redirect('components:all-categories')

        else:
            messages.info(request, 'form data is invalid')
    else:
        obj = get_object_or_404(ComponentCategory, id = id)
        form = CategoryForm(instance = obj)

        return render(request, 'components/update_category.html', {'form':form})

        
    


@staff_member_required(login_url='accounts:auth-login')
def delete_category(request, id):
    obj = get_object_or_404(ComponentCategory, id = id)
    obj.delete()
    messages.info(request, 'category deleted successfully')
    return redirect('components:all-categories')


#################################################################
##################       CRUD COMPONENTS        #################
#################################################################

@staff_member_required(login_url='accounts:auth-login')
def allcomponents(request):
    all_com = Component.objects.all()
    return render(request, 'components/all-components-admin.html', {'all_com':all_com})

@staff_member_required(login_url='accounts:auth-login')
def add_component(request):
    if request.method == "POST":
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'new component added successfully')
            return redirect('components:all-components-admin')
        else:
            messages.info(request, 'form data is invalid')
    else:
        form = ComponentForm()

    return render(request, 'components/create_component.html', {'form':form})


@staff_member_required(login_url='accounts:auth-login')
def update_component(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Component, id = id)
        form = ComponentForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            messages.info(request,'component updated successfully')

            return redirect('components:all-components-admin')

        else:
            messages.info(request, 'form data is invalid')
    else:
        obj = get_object_or_404(Component, id = id)
        form = ComponentForm(instance = obj)

    return render(request, 'components/update_component.html', {'form':form})



@staff_member_required(login_url='accounts:auth-login')
def delete_component(request, id):
    pass








