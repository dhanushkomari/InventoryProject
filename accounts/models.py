from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Department(models.Model):
    dept_name = models.CharField(max_length = 25)
    created_at = models.DateTimeField(auto_now_add=True)
    dept_description = models.TextField()
    dept_pic = models.ImageField(upload_to = 'Dept_profile_images', null = True, blank = True)
    
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ('-id',)
    
    def __str__(self):
        return '{}'.format(self.dept_name)




gender_choices = (
    ('male', 'male'),
    ('female', 'female')
)
class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key = True)
    employee_id = models.CharField(max_length = 10, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, null=True)
    mobile = models.CharField(max_length = 10, null=True, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=10, default = 'male', null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'profil_images', null = True, blank = True, )
    date_of_joining = models.DateField(auto_now = True, null=True, blank=True)
    designation = models.CharField(max_length=25, null=True, blank=True)
    status = models.BooleanField(default = True)
    employee_leaves = models.IntegerField(blank=True, null=True, default = 20)

    class Meta:
        verbose_name = 'User'
        verbose_name = 'User'
        ordering = ('-id', )
    
    def __str__(self):
        return '{}'.format(self.first_name+" "+self.last_name)