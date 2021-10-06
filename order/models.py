from django.db import models


###################################################
################  ORDER MODEL   ###################
###################################################
 
class Order(models.Model):    
    def auto_order_id(): 
        no = Order.objects.count()
        str1 = 'VSTNORDER'
        list2 = ['0','0','0','0','0', '0']
        item = no+1   
        str_item = str(item)   
        list_item = list(str_item)   
        leng = len(list_item)
        con = 6-leng   
        list2[con:] = list_item
        result = ''.join(map(str, list2))
        final = str1+result   
        return final

    order_id = models.CharField(max_length = 25,default=auto_order_id, editable = False)
    created_at = models.DateTimeField(auto_now_add = True)
    username = models.CharField(max_length =25, editable=False)
    email = models.CharField(max_length =100, editable=False)
    order_choices = (
        ('requested', 'requested'),
        ('approve', 'approve'),
        ('decline', 'decline'),
        ('deploy', 'deploy'),
        ('return', 'return'),
        
    )
    status = models.CharField(max_length = 50, choices = order_choices, default='requested')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.order_id)

###################################################
############  ORDER ITEM MODEL    #################
###################################################

class OrderItem(models.Model):
    component = models.CharField(max_length = 40)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        ordering = ('-id',)

    def __str__(self):
        return self.component


##################################################
###########    DEPLOYMENT MODEL   ################
##################################################

class Deployment(models.Model):
    def auto_dep_id(): 
        no = Deployment.objects.count()
        str1 = 'VSTDEP'
        list2 = ['0','0','0','0','0', '0']
        item = no+1   
        str_item = str(item)   
        list_item = list(str_item)   
        leng = len(list_item)
        con = 6-leng   
        list2[con:] = list_item
        result = ''.join(map(str, list2))
        final = str1+result   
        return final

    deployment_id = models.CharField(max_length = 20, editable = False, default = auto_dep_id)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length = 30, editable = False)
    email = models.CharField(max_length = 30, editable = False)

    class Meta:
        verbose_name = 'Deployment'
        verbose_name_plural = 'Deployment'
        ordering = ('-id',)

    def __str__(self):
        return str(self.deployment_id)

class DeployedItems(models.Model):
    component = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    deployment = models.ForeignKey(Deployment, on_delete = models.CASCADE)
    deployed_by = models.CharField(max_length = 40, blank=True, null = True)
    deployed_into = models.CharField(max_length=50, blank=True, null = True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Deployed Item'
        verbose_name_plural = 'Deployed Items'
        ordering = ('-id',)

    def __str__(self):
        return self.component