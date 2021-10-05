from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from components.models import Component
from accounts.models import CustomUser as User
from order.models import Order, Deployment
from leave.models import Leave
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def is_employee(user):
    return user.groups.filter(name='employee').exists()


############     USER DASHBOARD     #################
@user_passes_test(is_employee)
def user_dashboard(request, id):
    user = User.objects.get(id = id)
    orders = Order.objects.filter(username = user.username).order_by('-id')[:5]
    deployments = Deployment.objects.filter(username = user.username).order_by('-id')
    leaves = Leave.objects.filter(user = user.username).order_by('-id')[:5]

    ord_len = len(orders)
    dep_len = len(deployments)

    return render(request, 'dashboard/user_dashboard.html', {'orders':orders, 
                                                             'deployments':deployments,
                                                             'leaves': leaves, 
                                                             'ord_len':ord_len, 
                                                             'dep_len':dep_len,
                                                             })



##############   ADMIN DASHBOARD   ##################
@staff_member_required(login_url='accounts:auth-login')
def admin_dashboard(request):
    components = Component.objects.all().order_by('-id')[:5]
    users = User.objects.all().order_by('-id')[:5]
    orders = Order.objects.all().order_by('-id')[:5]
    deployments = Deployment.objects.all().order_by('-id')[:5]
    leaves = Leave.objects.all().order_by('-id')[:5]

    comp_len = Component.objects.count()
    user_len = User.objects.count()
    ord_len = Order.objects.count()
    dep_len = Deployment.objects.count()

    return render(request, 'dashboard/admin_dashboard.html', {'components':components, 
                                                              'users' : users,
                                                              'orders' : orders,
                                                              'deployments': deployments,
                                                              'leaves' : leaves,
                                                              'comp_len' : comp_len,
                                                              'user_len' : user_len,
                                                              'ord_len' : ord_len,
                                                              'dep_len' : dep_len,
                                                               })

    
    
