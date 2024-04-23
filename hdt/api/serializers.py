from rest_framework import serializers
from api.models import hdt
from api import hd
# from api import views

class hdtSerializer(serializers.HyperlinkedModelSerializer):
    Prediction=serializers.SerializerMethodField()
    class Meta:
        model=hdt
        # fields="__all__"
        fields=['id','age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','Prediction']
    def get_Prediction(self, data):
        age=data.age
        sex=data.sex
        cp=data.cp
        trestbps=data.trestbps
        chol=data.chol
        fbs=data.fbs
        restecg=data.restecg
        thalach=data.thalach
        exang=data.exang
        oldpeak=data.oldpeak
        slope=data.slope
        ca=data.ca
        thal=data.thal
        ob=(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        hdp = hd.pred(ob)
        return hdp