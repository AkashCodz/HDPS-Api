from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class signupform(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

sex_c = ((0, 'Female'),(1, 'Male'))
cp_c=((0, 'Asymptomatic'),(1, 'Atypical angina'),(2, 'Non-anginal pain'),(3, 'Typical angina'))
fbs_c=((0, 'False'),(1, 'True'))
res_c=((0, 'Showing probable or definite left ventricular hypertrophy by Estes’ criteria'),(1, 'Normal'),(2, 'ST-T wave abnormality'))
ex_c=((0, 'No'),(1, 'Yes'))
slo_c=((0, 'Downsloping'),(1, 'Flat'),(2,'Upsloping'))
ca_c=((0, '0'),(1, '1'),(2, '2'),(3, '3'))
th_c=((0, 'NULL'),(1, 'Fixed defect'),(2,'Normal blood flow'),(3,'Reversible defect'))

class userforms(forms.Form):
    
    age=forms.CharField(label='Age',required=True,widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Enter the Age'}))
    sex=forms.ChoiceField(label='Sex',choices=sex_c,required=True)
    cp=forms.ChoiceField(label='CP',choices=cp_c,required=True)
    trestbps=forms.CharField(label='trestbps',required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    chol=forms.CharField(label='chol',required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    fbs=forms.ChoiceField(label='fbs',choices=fbs_c,required=True)
    restecg=forms.ChoiceField(label='restecg',choices=res_c,required=True)
    thalach=forms.CharField(label='thalach',required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    exang=forms.ChoiceField(label='exang',choices=ex_c,required=True)
    oldpeak=forms.CharField(label='oldpeak',required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    slope=forms.ChoiceField(label='slope',choices=slo_c,required=True)
    ca=forms.ChoiceField(label='ca',choices=ca_c,required=True)
    thal=forms.ChoiceField(label='thal',choices=th_c,required=True)