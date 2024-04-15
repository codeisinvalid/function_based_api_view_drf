from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()
# def student_create(request):
#     return Response({'msg':'Hello, World'})
    
# @api_view(['GET'])
# def student_create(request):
#     return Response({'msg':'Hello, World'})
    
# @api_view(['POST'])
# def student_create(request):
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg':'Hello, World! This is post request'})
    
@api_view(['GET','POST'])
def student_create(request):
    if request.method == 'GET':
        return Response({'msg':'Hello, world! This is get request.'})
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'Hello, World! This is post request', 'data':request.data})
    
