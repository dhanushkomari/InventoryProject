from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .models import Bag, BagItem
from accounts.models import CustomUser as User
from components.models import Component
from order.models import Order, OrderItem


#########################################################
###########      CHECKING USERS     #####################
#########################################################
def is_employee(user):
    return user.groups.filter(name='employee').exists()

def is_hr(user):
    return user.group.filter(name = 'hr').exists()


#########################################################
################     CREATING BAG ID    #################
#########################################################
def _bag_id(request):
    cart = request.user.username
    # print(cart)
    if not cart:
        cart = request.user.username
    return cart


#########################################################
##############    ADDING COMPONENT TO BAG    ############
#########################################################
@user_passes_test(is_employee)
def add_to_bag(request, component_id):
    component = Component.objects.get(component_id = component_id)
    user = request.user    
    try:
        bag = Bag.objects.get(bag_id = _bag_id(request))
    except Bag.DoesNotExist:
        bag = Bag.objects.create(bag_id = _bag_id(request))
        bag.save()
    try:
        bag_item = BagItem.objects.get(component = component, bag = bag)
        if bag_item.quantity < bag_item.component.stock:
            bag_item.quantity += 1
            bag_item.save()
    except BagItem.DoesNotExist:
        bag_item = BagItem.objects.create(component = component,quantity = 1, bag = bag)
        bag_item.save()    
    
    messages.success(request,'Component is added to bag!')
    return redirect('bag:bag_details')
    # return redirect(request.META.get('HTTP_REFERER'))


#########################################################
################    BAG DETAILS     #####################
#########################################################
@user_passes_test(is_employee)
def bag_details(request):
    try:
        bag = Bag.objects.get(bag_id = _bag_id(request))
        bag_items = BagItem.objects.filter(bag = bag, active = True)
    except ObjectDoesNotExist:
        bag = Bag.objects.create(bag_id = _bag_id(request))
        bag.save()
        bag_items = 'no items'
    return render(request, 'bag/bag.html', {'bag_items':bag_items})
    

#########################################################
##############  REMOVING ITEM FROM BAG    ###############
#########################################################
@user_passes_test(is_employee)
def remove_item(request, component_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    component = get_object_or_404(Component, id=component_id)
    bag_item = BagItem.objects.get(component = component, bag = bag)

    if bag_item.quantity > 1:
        bag_item.quantity -= 1
        bag_item.save()
    else:
        bag_item.delete() 
    return redirect('bag:bag_details')


#########################################################
###########  DELETING ALL THE BAG ITEMS    ##############
#########################################################
@user_passes_test(is_employee)
def delete_bag_items(request, component_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    component = get_object_or_404(Component, id=component_id)
    bag_item = BagItem.objects.get(component = component, bag = bag)
    bag_item.delete() 
    messages.success(request, 'item removed successfully')   
    return redirect('bag:bag_details')


########################################################
#############   REQUESTING COMPONENTS    ###############
########################################################
@user_passes_test(is_employee)
def request_components(request):
    try:
        bag = Bag.objects.get(bag_id = _bag_id(request))
        bag_items = BagItem.objects.filter(bag = bag, active = True)
        
        order_details = Order.objects.create(
                                             username = request.user.username,
                                             email = request.user.email,
                                             status = 'requested'              
                                            )
        order_details.save()

        for order_item in bag_items:
            oi = OrderItem.objects.create(
                component = order_item.component.name,
                quantity = order_item.quantity,
                order = order_details,
            )
            oi.save()

            component = Component.objects.get(id = order_item.component.id)
            component.stock = int(order_item.component.stock -  order_item.quantity)
            order_item.delete() 
            component.save()

    except ObjectDoesNotExist:
        pass
    return redirect('order:order_success')
    

