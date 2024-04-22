from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.http import Http404
from rest_framework import status


@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        # print("Query Params:", request.query_params)
        id = pk
        # print("ID:", id)
        if id is not None: 
            try:          
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data)  
            except Student.DoesNotExist:
                raise Http404("Student does not exist") 
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        
    if request.method=="POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        student = Student.objects.get(pk = id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PATCH':
        id = pk
        student = Student.objects.get(pk = id)
        serializer = StudentSerializer(student, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    
    if request.method == 'DELETE':
        id = pk
        student = Student.objects.get(pk = id)
        student.delete()
        return Response({'msg':'Data Deleted'})