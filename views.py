from collections import Counter
from django.shortcuts import render
from myapi.models import Attritiondata
from myapi.forms import attritionForm
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import joblib
import numpy as np
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from myapi.serializers import serializerclass
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
import os


# Create your views here.
class attritionView(viewsets.ModelViewSet):
    queryset= Attritiondata.objects.all()
    serializers_class= serializerclass
    
@api_view(['GET','POST'])
def predict_attrition(request):
    if request.method == "POST":
        Department= request.data.get('Department')
        if Department is not None:
             qs=Attritiondata.objects.filter(department=Department) 
             serializers_class=serializerclass(qs,many=True)  
             return Response(serializers_class.data,content_type="application/json")
        qs=Attritiondata.objects.all
        serializers_class=serializerclass(qs,many=True)  
        return HttpResponse(serializers_class.data)
   # else:
            #return JsonResponse({'error': 'Invalid form data'}, status=400)
    
    
def load_model(df1):
    load_model_path = './mlmodel/attr_pipe.pkl'
    model = joblib.load(load_model_path)
    y_pred = model.predict(df1)
    return y_pred

def queryset_to_list(qs,fields=None, exclude=None):
    return [model_to_dict(x,fields,exclude) for x in qs]

def show(request):
    result=None
    table_html=None
    final_yes=None
    percent=None
    wordcount=None
    rowcount=None
    allcount=None
    employee=None
    if request.method == "POST":
        form = attritionForm(request.POST)
        if form.is_valid():
            Departmentdata= form.cleaned_data['Department']
            if Departmentdata=='All Department':
                qs=Attritiondata.objects.all()
                allcount=qs.count()
                list=queryset_to_list(qs)
                df = pd.DataFrame(list)
                df.drop(columns=['id'],inplace=True)
                #'csrfmiddlewaretoken',
                df1= df.to_numpy()
                result=(load_model(df1))
                result1=pd.DataFrame(result, columns=['Attrition'])
                result2 = pd.concat([df, result1], axis=1)
                predicted=result2.groupby('Attrition')
                final_yes=predicted.get_group('Yes')
                Numword=Counter(result.tolist())
                wordcount=Numword["Yes"]
                floatnum=float((wordcount/allcount)*100)
                percent=round(floatnum,2)
            else:
                qs=Attritiondata.objects.filter(Department=Departmentdata)
                #print(Departmentdata)
                rowcount=qs.count() # specific department employee number
                #employee=qs.values_list('EmployeeNumber','JobRole','id').order_by('id')
                list=queryset_to_list(qs)
                df = pd.DataFrame(list)
                df.drop(columns=['id'],inplace=True)
                #'csrfmiddlewaretoken',
                df1= df.to_numpy()
                result=(load_model(df1))
                # print(type(result))
                result1=pd.DataFrame(result, columns=['Attrition'])
                result2 = pd.concat([df, result1], axis=1)
                predicted=result2.groupby('Attrition')
                final_yes=predicted.get_group('Yes')
                Numword=Counter(result.tolist())
                wordcount=Numword["Yes"]
                floatnum=float((wordcount/rowcount)*100)
                percent=round(floatnum,2)
    
    form= attritionForm()                  
    return render(request, "test.html", {"form": form,"result": final_yes if result is not None else None ,"percent":percent ,"rowcount":rowcount if rowcount is not None else None ,"allcount":allcount , "number":wordcount ,"employee": employee if employee is not None else None})



# def show(request):
#     if request.method == "POST":
#         try:
#             post_data = json.loads(request.body.decode('utf-8'))
#             df = pd.DataFrame([post_data])
#             model = load_model()
#             result = prediction(model,df)
#             return JsonResponse({'result':result})
#         except json.JSONDecodeError as e:
#             return JsonResponse({'error':'Invalid Json format'},status=400)
        
#     return JsonResponse({'error':'Invalid Json format2'},status=400)
    

