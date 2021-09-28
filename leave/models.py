from django.db import models

# Create your models here.

class Leave(models.Model):

    def auto_comp_id(): 
        no = Leave.objects.count()
        str1 = 'VSTNLEAVE'
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
    
    leave_choices = (
        ('sick', 'sick'),
        ('planned', 'planned'),
        ('unplanned', 'unplanned'),
    )
    status_choices = (
        ('requested', 'requested'),
        ('approved', 'approved'),
        ('declined', 'declined'),
    )

    leave_id = models.CharField(max_length=25, editable=False, default=auto_comp_id)
    user = models.CharField(max_length = 40)
    email = models.CharField(max_length=50)
    leave_type = models.CharField(choices=leave_choices, max_length=20, default = 'planned')
    from_date = models.DateField()
    to_date = models.DateField()
    total_no_of_leaves = models.IntegerField()
    reason = models.CharField(max_length = 100, blank=True, null = True)
    status = models.CharField(choices=status_choices, max_length =20, default = 'requested')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Leave'
        verbose_name_plural = 'Leaves'

    def __str__(self):
        return self.leave_id    