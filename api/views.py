from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.http import Http404


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        print("Query Params:", request.query_params)

        id = request.query_params.get('id')
        print("ID:", id)

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