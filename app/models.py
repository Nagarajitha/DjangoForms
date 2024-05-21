from django.db import models

# Create your models here.
'''
    

class School(models.Model):
    sname = models.CharField(max_length=100 )
    sage = models.IntegerField()
    semail = models.EmailField()
    surl = models.URLField()
    spassword = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    gender = models.chq
    #scourses = forms.ChoiceField(choices=c).widget=forms.SelectMultiple # for multiple selections
    scourses = forms.ChoiceField(choices=c,widget=forms.CheckboxSelectMultiple) # for multiple selections
'''

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name