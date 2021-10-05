from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import user_passes_test
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from order.models import Order, OrderItem, Deployment, DeployedItems
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from components.models import Component
from accounts.models import CustomUser as User

# Create your views here.

def is_employee(user):
    return user.groups.filter(name='employee').exists()


###############    ORDER FUNCTIONALITIES FOR EMPLOYEE    ########################
@user_passes_test(is_employee)
def order_success(request):
    return render(request, 'order/order_success.html')

@user_passes_test(is_employee)
def user_orders(request):
    orders = Order.objects.filter(username = request.user.username)
    print(orders)

    return render(request, 'order/orders.html', {'orders':orders})

@user_passes_test(is_employee)
def order_detail(request, id):
    order = Order.objects.get(id = id)
    print(order)
    oi = OrderItem.objects.filter(order_id = order)
    print(oi)

    return render(request, 'order/order_detail.html', {'oi':oi, 'order':order})



################   ORDER FUNCTIONALITIES BY ADMIN    ########################
@staff_member_required(login_url='accounts:auth-login')
def all_order(request):
    orders = Order.objects.all()
    return render(request, 'order/all_orders.html',{'orders':orders})

@staff_member_required(login_url='accounts:auth-login')
def order_detail_admin(request, id):
    order = Order.objects.get(id = id)
    print(order)
    oi = OrderItem.objects.filter(order_id = order)
    print(oi)

    return render(request, 'order/order_detail_admin.html', {'oi':oi, 'order':order})


@staff_member_required(login_url='accounts:auth-login')
def order_accept(request, id):
    order = Order.objects.get(id = id)
    if order.status == 'requested':
        order.status = 'approve'
        order.save()
        messages.info(request, 'Component request has approved')   
    return redirect('order:all-orders')


@staff_member_required(login_url='accounts:auth-login')
def order_decline(request, id):
    order = Order.objects.get(id = id)
    if order.status == 'requested':
        print('status = requested')
        order.status = 'decline'
        order.save()

        oi = OrderItem.objects.filter(order_id = order)
        print(oi)

        for i in oi:
            oi_id = i.order_id
            oi_name = i.component
            oi_quantity = i.quantity

            print(oi_quantity)
            
            component = Component.objects.get(name = oi_name)
            print()
            print(component.stock)
            print()
            component.stock = component.stock + oi_quantity
            component.save()

        messages.info(request, 'Component request has declined')   
    return redirect('order:all-orders')

@staff_member_required(login_url='accounts:auth-login')
def order_return(request, id):
    order = Order.objects.get(id = id)
    oi = OrderItem.objects.filter(order_id = order)

    if order.status == 'approve':
        order.status = 'return'
        order.save()

        for i in oi:
            oi_name = i.component
            oi_quantity = i.quantity

            component = Component.objects.get(name = oi_name)
            
            component.stock = component.stock + oi_quantity
            component.save()

            messages.info(request, 'component returned successfully')

    return redirect('order:all-orders')



@staff_member_required(login_url='accounts:auth-login')
def order_deploy(request, id):
    order = Order.objects.get(id = id)
    oi = OrderItem.objects.filter(order_id = order)

    if request.method == "POST":
        
        # try:
        if order.status == 'approve':
            order.status = 'deploy'
            order.save()
            
            deployment = Deployment.objects.create(
                                                    username = order.username,
                                                    email = order.email    
                                                    )
            deployment.save()                


            for i in oi:
                oi_name = i.component
                oi_quantity = i.quantity

                deployment_item = DeployedItems.objects.create(
                                                                    component = oi_name,
                                                                    quantity = oi_quantity,
                                                                    deployment = deployment,
                                                                    deployed_by = order.username,
                                                                    deployed_into = request.POST['deployed_into'] 
                                                                )
                deployment_item.save()
                messages.info(request, 'items added to deployment list')
    
        # except ObjectDoesNotExist:
        #     pass
    return redirect('order:all-orders')

@staff_member_required(login_url='accounts:auth-login')
def deployed_list_admin(request):
    deployment = Deployment.objects.all().order_by('-id')
    return render(request, 'order/deploy_list_admin.html', {'deployment':deployment})

@user_passes_test(is_employee)
def deployed_list_user(request, id):
    user = User.objects.get(id = id)
    deployment = Deployment.objects.filter(username = user.username)    
    return render(request, 'order/deploy_list_user.html', {'deployment':deployment})

def deployed_detail(request, id):
    deployment = Deployment.objects.get(id =id)
    dep_items = DeployedItems.objects.filter(deployment = deployment)

    print(dep_items)

    return render(request, 'order/deploy_detail.html', {'deployment':deployment, 'dep_items':dep_items})