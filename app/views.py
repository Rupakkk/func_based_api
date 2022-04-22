from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# @api_view()    # When we don't write anything then it is get @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello K chha'})


@api_view(['GET','POST'])  # We must initiaize method like this at the top first except GET
def hello_world(request):
    if request.method == 'POST':
        return Response({'msg':'This is POST REQUEST','data':request.data})
    if request.method == "GET":
        print(request.data)
        return Response({'msg':'This is GET response','data':request.data})