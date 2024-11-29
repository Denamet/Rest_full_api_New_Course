from rest_framework.views import APIView
from rest_framework import response , status
from django.shortcuts import render
from . import serializers



class Hello_Api(APIView):
    serliesers_class = serializers.hello_serializers


    def get(self , request , format=None):
        """ Returns a list Api Viwes features """

        api = ["uses Http methods function get post patch put "]

        res = {"massage_one" : "hello world" , "massage two " : api}
        
        return  response.Response(res)
    

    def post(self , request):

        serilazier = self.serliesers_class(data=request.data)
        if serilazier.is_valid():
            name = serilazier.validated_data.get("name")
            massge = f"hello {name}"
            print(serilazier.validated_data["name"])
         
            return response.Response({"massge":massge})
        else :
            return response.Response(serilazier.errors,
                                     status=status.HTTP_400_BAD_REQUEST , )
    

    def put(self , request , pk=None):
        

        return response.Response({"method":"put"})


    def patch(self , request , pk=None):
        return response.Response({"method":"patch"})
    

    def delete(self , request , pk=None):
        return response.Response({"method":"delete"})







def calculator(request):

   


    result = None
    error_message = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operator = request.POST.get('operator')

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error_message = "Cannot divide by zero!"
            else:
                error_message = "Invalid operator!"
        except ValueError:
            error_message = "Invalid input!"

    return render(request, 'Calculator.html' , {'result': result, 'error_message': error_message})
