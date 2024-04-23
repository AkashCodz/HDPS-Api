from rest_framework import viewsets
from api.models import hdt
from api.serializers import hdtSerializer
from rest_framework.response import Response
from api import hd

class hdtViewSet(viewsets.ModelViewSet):
    queryset = hdt.objects.order_by('-id')
    serializer_class = hdtSerializer
    # def create(self, request):
    #     viewsets.ModelViewSet.create(self, request)
    #     data=request.data
    #     age=data['age']
    #     sex=data['sex']
    #     cp=data['cp']
    #     trestbps=data['trestbps']
    #     chol=data['chol']
    #     fbs=data['fbs']
    #     restecg=data['restecg']
    #     thalach=data['thalach']
    #     exang=data['exang']
    #     oldpeak=data['oldpeak']
    #     slope=data['slope']
    #     ca=data['ca']
    #     thal=data['thal']
    #     ob=(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    #     hdp = hd.pred(ob)
    #     return Response({'status': 'Success', 'Heart-disease': hdp})


""" from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response

class Prediction(APIView):
    def post(self, request):
        data = request.data
        age = data['age']
        sex = data['sex']
        cp = data['cp']
        trestbps = data['trestbps']
        chol = data['chol']
        fbs = data['fbs']
        restecg = data['restecg']
        thalach = data['thalach']
        exang = data['exang']
        oldpeak = data['oldpeak']
        slope = data['slope']
        ca = data['ca']
        thal = data['thal']
        model = ApiConfig.model
        model_predicted = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        response_dict = {"Predicted value": model_predicted}
        print(response_dict)
        return Response(response_dict, status=200) """