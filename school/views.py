import django.contrib.auth.models
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,permissions
from .serializers import(ProgramSerializer,UserSerializer,EventSerializer,TeacherSerializer,TestimonialSerializer,StudentSerializer,GradeSerializer,ReviewSerializer,FeedbackUserSerializer,ProfileSerializer,SubjectSerializer)
from .models import Program,Event,Teacher,Testimonial,Student,Grade,Review,FeedbackUser,User,Profile,Subject

# Create your views here.

class ProgramViewSet(viewsets.ModelViewSet):
    queryset=Program.objects.all()
    serializer_class=ProgramSerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by("-created_at")
    serializer_class = TestimonialSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
            feedback_user, created =FeedbackUser.objects.get_or_create(email = self.request.data.get("email"), defaults={"name":self.request.data.get("name")})
            serializer.save(user=feedback_user)
        
        
        
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    
class FeedbackUserViewSet(viewsets.ModelViewSet):
    queryset=FeedbackUser.objects.all()
    serializer_class=FeedbackUserSerializer    
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes =[permissions.IsAuthenticated]
    
class GradeViewSet(viewsets.ModelViewSet):
    queryset=Grade.objects.all()
    serializer_class=GradeSerializer
    
    
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes =[permissions.IsAuthenticated]
    def perform_create(self,serializer):
        feedback_user, created=FeedbackUser.objects.get_or_create(email = self.request.data.get("email"), defaults={"name":self.request.data.get("name")})
        serializer.save(user=feedback_user)
        
class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer
    permission_classes =[permissions.IsAuthenticated]
    


class ProfileViewSet(viewsets.ModelViewSet):
    
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes =[permissions.IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        return Profile.objects.filter(user=user) 
    

