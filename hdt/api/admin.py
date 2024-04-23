from django.contrib import admin
from api.models import hdt

class Admin(admin.ModelAdmin):
    list_display=('id','age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal')
  
admin.site.register(hdt, Admin)
# admin.site.register(hdt)
    