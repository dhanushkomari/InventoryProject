from django.db import models
from django.urls import reverse

# Create your models here.


##################   COMPONENT CATEGOTY    #####################
class ComponentCategory(models.Model):
    name = models.CharField(max_length=75, unique = True)
    # slug = models.SlugField(max_length=100, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'component_category', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Component Category'
        verbose_name_plural = 'Component Categories'
    
    def __str__(self):
        return '{}'.format(self.name)
    
    def get_url(self):
        return reverse('components:component-list-cat', args=[self.id])
            
    
 
################           COMPONENT       ######################
class Component(models.Model):
    
    def auto_comp_id(): 
        no = Component.objects.count()
        str1 = 'VSTNHC'
        list2 = ['0','0','0','0','0']
        item = no+1   
        str_item = str(item)   
        list_item = list(str_item)   
        leng = len(list_item)
        con = 5-leng   
        list2[con:] = list_item
        result = ''.join(map(str, list2))
        final = str1+result   
        return final  
        
    component_id = models.CharField(max_length = 20, default = auto_comp_id, editable=False)
    name = models.CharField(max_length=75, unique = True)
    # slug = models.SlugField(unique=True, max_length = 100)
    category = models.ForeignKey(ComponentCategory, on_delete=models.CASCADE)
    component_location = models.CharField(max_length =  100, default='inventory')
    vendor = models.CharField(max_length=100, null = True, blank=True)
    invoice = models.CharField(max_length=25, blank=True, null=True)
    date_of_order = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'components', blank=True, null=True)
    avialable = models.BooleanField(default=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits =10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('id','name','category',)
        verbose_name = 'Component'
        verbose_name = 'Components'
    
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        pass


    



