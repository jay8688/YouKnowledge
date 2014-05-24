from django.db import models

class Info(models.Model):
    dataset = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date uploaded')
    
    def __unicode__(self):
        return self.dataset