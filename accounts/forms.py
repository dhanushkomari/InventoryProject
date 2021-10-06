from .models import CustomUser as User
from django import forms
from .models import Department

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile', 'department', 'designation', 'employee_id', 'employee_leaves')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('dept_name', 'dept_description')
