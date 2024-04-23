from django.db import models

class hdt(models.Model):
    age=models.IntegerField()
    sex=models.IntegerField()
    cp=models.IntegerField()
    trestbps=models.IntegerField()
    chol=models.IntegerField()
    fbs=models.IntegerField()
    restecg=models.IntegerField()
    thalach=models.IntegerField()
    exang=models.IntegerField()
    oldpeak=models.FloatField()
    slope=models.IntegerField()
    ca=models.IntegerField()
    thal=models.IntegerField()
    def to_dict(self):
        return{
            'age':self.age,
            'sex':self.sex,
            'cp':self.cp,
            'trestbps':self.trestbps,
            'chol':self.chol,
            'fbs':self.fbs,
            'restecg':self.restecg,
            'thalach':self.thalach,
            'exang':self.exang,
            'oldpeak':self.oldpeak,
            'slope':self.slope,
            'ca':self.ca,
            'thal':self.thal
        }