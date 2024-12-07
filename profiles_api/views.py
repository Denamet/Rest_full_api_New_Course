from rest_framework.views import APIView
from rest_framework import response , status
from django.shortcuts import render
from . import serializers
from django.views import View
from rest_framework.viewsets import ViewSet



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









class HelloViewSet(ViewSet):

    
    serliesers_class = serializers.hello_serializers

    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return response.Response({'message': 'Hello!', 'a_viewset': a_viewset})
    

    def create(self , request ):
       

        print(request.method)
        print(request.data)
        print(type(request.data))
        
        
        serializer = self.serliesers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return response.Response({"massge":"hello "+name } )
        
        
        else :
            return response.Response({"massge":"please Type data valid "})
            


    def retrieve(self , request , pk=None):
        print(pk)
        return response.Response({"http_method":"GET" , "pk" : pk})
    


    def update(self , request , pk=None ):
        print(pk)
        return response.Response({"http_method":"PUT" , "pk" : pk})





    def partial_update(self , request , pk=None ):
            print(pk)
            return response.Response({"http_method":"PATCH" , "pk" : pk})



    def destroy(self , request , pk=None ):
        print(pk)
        return response.Response({"http_method":"DELETE" , "pk" : pk})




