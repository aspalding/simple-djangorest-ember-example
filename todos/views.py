from rest_framework import viewsets, generics

from todos.models import Todo
from todos.serializers import TodoSerializer

    
class Todos(generics.ListCreateAPIView):
    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class Todo(generics.RetrieveUpdateDestroyAPIView):
    model = Todo
    serializer_class = TodoSerializer
