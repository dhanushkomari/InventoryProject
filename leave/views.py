from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .forms import LeaveForm
from django.contrib import messages
from .models import Leave
import datetime
from accounts.models import CustomUser as User



# Create your views here.

#########################################################
###########      CHECKING USERS     #####################
#########################################################
def is_employee(user):
    return user.groups.filter(name='employee').exists()

def is_hr(user):
    return user.group.filter(name = 'hr').exists()

#########################################################
###############    APPLYING LEAVE   #####################
#########################################################
@user_passes_test(is_employee)
def apply_leave(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)

        user = request.user.username
        email = request.user.email
        leave_type = request.POST['leave_type']
        total_no_of_leaves = request.POST['total_no_of_leaves']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        reason = request.POST['reason']

        # print(user, email, leave_type, total_no_of_leaves, from_date, to_date, reason)

        start_date = datetime.datetime.strptime(from_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(to_date, "%Y-%m-%d")
        diff = abs((end_date-start_date).days)

        total_days = diff+1
        
        if not from_date>to_date:
            l = Leave.objects.create(
                                        user = user,
                                        email = email,
                                        leave_type = leave_type,
                                        total_no_of_leaves = total_days,
                                        from_date = from_date,
                                        to_date = to_date,
                                        reason = reason,
                                    )
            l.save()
            messages.info(request, 'leave applied successfully')
            # return redirect('')
        else:
            messages.info(request, 'invalid dates submitted')

    else:
        form = LeaveForm     
    return render(request, 'leave/apply_leave.html', {'form':form})


#########################################################
##############    LEAVES LIST ADMIN    ##################
#########################################################
@staff_member_required(login_url='accounts:auth-login')
def leave_list_admin(request):
    all_leaves = Leave.objects.all()
    return render(request, 'leave/all_leaves_list.html', {'all_leaves': all_leaves})

#########################################################
################ LEAVE LIST USER     ####################
#########################################################
@user_passes_test(is_employee)
def leaves_list_user(request, username):
    all_leaves = Leave.objects.filter(user = username)
    return render(request, 'leave/user_leaves_list.html', {'all_leaves': all_leaves})


@staff_member_required(login_url='accounts:auth-login')
def leave_detail_admin(request, id):
    leave = Leave.objects.get(id = id)
    return render(request, 'leave/leave_detail_admin.html', {'leave':leave})



#########################################################
###############    APPROVING LEAVE   ####################
#########################################################
@staff_member_required(login_url='accounts:auth-login')
def approve_leave(request, id):
    leave = Leave.objects.get(id = id)

    if leave.status == 'requested':
        leave.status = 'approved'

        user = User.objects.get(username = leave.user)        
        user.employee_leaves = (user.employee_leaves - leave.total_no_of_leaves)

        if user.employee_leaves > 0:
            user.save()
            leave.save()
            messages.info(request, 'Leave approved')
        else:
            messages.info(request, "user don't have leaves")
        
    return redirect('leave:all-leaves')

#########################################################
###############    DECLINING LEAVE   ####################
#########################################################
@staff_member_required(login_url='accounts:auth-login')
def decline_leave(request, id):
    leave = Leave.objects.get(id = id)

    if leave.status == 'requested':
        leave.status = 'declined'
        leave.save()
        messages.info(request, 'Leave declined')
    
    return redirect('leave:all-leaves')

