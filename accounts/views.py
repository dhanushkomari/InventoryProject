from django.contrib import auth
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser as User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserForm, UserProfileForm


def is_employee(user):
    return user.groups.filter(name='employee').exists()



#################     LOGIN     ######################
def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                login(request,user)
                # messages.success(request, 'You have logged in successfully')
                if user.is_superuser:
                    return redirect('dashboard:admin-dashboard')


                else:
                    return redirect('components:component-list-all')
                # redirect to dashboard
        else:
            messages.warning(request, 'Invalid credentials')    
    return render(request, 'accounts/auth-login.html')


################   LOGOUT     ##############################
@login_required
def LogoutView(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('accounts:auth-login')
    

###############   Register employee    ###############
@user_passes_test(lambda u:u.is_superuser)
def RegisterEmployee(request):
    if request.method == "POST": 
        # fetching form data       
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        employee_id = request.POST['employee_id']        
        
        
        if User.objects.filter(username = username).exists():          # checking for username
            messages.warning(request, 'username already taken')
        
        elif User.objects.filter(email = email).exists():              # checking for email
            messages.warning(request, 'Email already exists')
        
        elif User.objects.filter(employee_id = employee_id).exists():   # checking for employee_id
            messages.warning(request, 'Employee ID already exists')

        else:
            if password1 == password2:     # checking for password match
                user = User(username = username,
                            first_name = first_name,
                            last_name = last_name,
                            email = email,
                            password = password1,
                            employee_id = employee_id,
                            )
                user.set_password(password1)
                user.save()
                Employee_group = Group.objects.get(name = 'employee')      # Fetching employee group
                Employee_group.user_set.add(user)                          # Adding user to employee group

                messages.success(request, 'New user has added successfully')     
                # return HttpResponse('employee created')
                return redirect('accounts:all-employes')
            
            else:
                messages.warning(request, 'passwords do not matched')

    return render(request, 'accounts/auth-register.html')


###########    ALL EMPLOYEES     ######################
@staff_member_required(login_url='accounts:auth-login')
def allEmployees(request):
    emp = User.objects.filter(groups = 1)  
    print(emp)  
    # return HttpResponse('Hii')
    return render(request, 'accounts/all_employees.html', {'emp':emp})


###############    EDIT EMPLOYEES     ######################
@staff_member_required(login_url='accounts:auth-login')
def editEmployee(request, id):
    if request.method == "POST":
        obj = get_object_or_404(User, id = id)
        form = UserForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            messages.info(request, 'employee profile updated')
            return redirect('accounts:all-employes')
        else:
            messages.info(request, 'invalid form data')
    else:
        obj = get_object_or_404(User, id = id)
        form = UserForm(instance =obj)
    return render(request, 'accounts/edit_employee.html', {'form':form})

###############  EDIT PROFILE(FOR EMPLOYEE SIDE)   #########
# @user_passes_test(is_employee)
def editUserProfile(request, id):
    if request.method == "POST":
        obj = get_object_or_404(User, id = id)
        form = UserProfileForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            messages.info(request, 'employee profile updated')
            return redirect('accounts:all-employes')
            # REDIRECTION IS NOT SET AFTER UPDATING(REDIRECT TO DASHBOARD)
        else:
            messages.info(request, 'invalid form data')
    else:
        obj = get_object_or_404(User, id = id)
        form = UserProfileForm(instance =obj)
    return render(request, 'accounts/edit_user_profile.html', {'form':form})




#############    DELETE EMPLOYEES     ######################
@staff_member_required(login_url='accounts:auth-login')
def deleteEmployee(request, id):
    employee = User.objects.get(id = id)
    employee.delete()
    messages.info(request, 'User deleted successfully')
    return redirect('accounts:all-employes')


###############    CHANGE PASSWORD     ################
def ChangePasswordView(request, id):
    obj = User.objects.get(id = id)
    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            obj.set_password(password1)
            obj.save()
            messages.info(request, 'password changed successfully')
            return redirect('accounts:all-employes')
        else:
            messages.info(request, 'passwords not matched') 
    return render(request, 'accounts/reset_password.html')


