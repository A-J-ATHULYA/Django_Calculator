from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self, request):
        request_body = request.body         # type of request body is json
        # {\r\n  "num1": 100,\r\n "num2": 25\r\n}
        form_data = loads(request_body)     # type of request body is dict
        # convert json to dict
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 + n1
        # print(request_body)
        data = {
            "message" : "API addition called successfully......!",
            "Sum" : result
            }
        
        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class Subtraction(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        # print(form_data)
        # print(type(form_data))
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 - n2
        
        
        return JsonResponse(
            {"message" : "Subtraction API is working....!",
            "Difference" : result}
            )
        
@method_decorator(csrf_exempt, name='dispatch')
class Multiplication(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        # print(form_data)
        # print(type(form_data))
        
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 * n2
        return JsonResponse({
            "message" : "Multiplication API is working....!",
            "Product" : result
        })
        
@method_decorator(csrf_exempt, name='dispatch')
class Division(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        # print(form_data)
        # print(type(form_data))
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 // n2
        
        return JsonResponse({
            "message": "Division API is working....!", 
            "Division" : result
        })
        
@method_decorator(csrf_exempt, name='dispatch')
class Modulus(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        # print(form_data)
        # print(type(form_data))
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 / n2
        return JsonResponse({
                    "message": "Modulus API is working....!", 
                    "Modulus" : result
                })
        
        
# BMI Calculation
@method_decorator(csrf_exempt, name='dispatch')
class BMI(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        
        height = form_data.get("Height")
        weight = form_data.get("Weight")
        bmi = weight/(height/100)**2
        return JsonResponse({
                    "message": "BMI API is working....!",
    
    
    
                    "Height" : height,
                    "Weight" : weight,
                    "BMI" : bmi
                    })


#Age calculation        
@method_decorator(csrf_exempt, name='dispatch')
class Age(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        birth = form_data.get("Birth_year")
        current = form_data.get("Current_year")
        age = current - birth
        return JsonResponse({
                        "message": "Age API is working....!",
                        "Age": age
                        })
       
       
#Percentage calculation
@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        total_marks = form_data.get("total_mark")
        marks_obtained = form_data.get("obtained_mark")
        percentage = (marks_obtained/total_marks)*100
        return JsonResponse({
                        "message": "percentage API is working....!",
                        "Percentage" : percentage
                        })
        
        
#Area calculation of rectangle
@method_decorator(csrf_exempt, name='dispatch')
class AreaView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        l = form_data.get("length")
        w = form_data.get("width")
        area = l * w
        return JsonResponse({
                        "message": "Area API is working....!",
                        "Length" : l,
                        "Width" : w,
                        "Area" : area
                        })
        
        
@method_decorator(csrf_exempt, name='dispatch')
class SimpleInterest(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        p = form_data.get("principal")
        r = form_data.get("rate")
        t = form_data.get("time")
        si = (p * r * t) / 100
        return JsonResponse({
                        "message": "Simple Interest API is working....!",
                        "Principal" : p,
                        "Rate" : r,
                        "Time" : t,
                        "Simple Interest" : si
                        })
        