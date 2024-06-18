from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Views for Users Notes after Authentication
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # cant call unless valid JWT passed

    # returns authenticated.user = self.request.user
    def get_queryset(self):
        user = self.request.user
        # Filter all notes written by just this user
        # Default protected path of only your notes. 
        return Note.objects.filter(author=user)

    # Custom Method for Views
    # Overwriting create method for some customization of it
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else :
            print(serializer.errors)

# Built in generic View
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny] # for testing would need to migrate again

    # makes sure only deleting notes owned by that user
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# View for User
class CreateUserView(generics.CreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]