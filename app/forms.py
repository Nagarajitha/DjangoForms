from django import forms


# #inorder to create django forms

#  first create forms.py in app
# create a class for form 
# create view for this class in app.views


g = [['Male','male'],['FEMALE','female']] # 1st value sent to backend ,2 nd value displaed in frontend
c= [['Python','python'],['Java','java'],['Sql','sql']]
class StudentForm(forms.Form):  
    sname =forms.CharField(max_length=100)
    sage = forms.IntegerField()
    semail = forms.EmailField()
    surl = forms.URLField()
    spassword = forms.CharField(widget=forms.PasswordInput) #no password field ,inorder to create password feild we use charfiled+widget = form.passwordinput
    address = forms.CharField(widget=forms.Textarea()) # for textarea charfeild+ widget = forms.textarea
    gender = forms.ChoiceField(choices=g,widget=forms.RadioSelect)#for radio buttons
    #scourses = forms.ChoiceField(choices=c).widget=forms.SelectMultiple # for multiple selections
    scourses = forms.ChoiceField(choices=c,widget=forms.CheckboxSelectMultiple) # for multiple selections


class TopicForm(forms.Form):
    topic_name = forms.CharField(max_length=100)






