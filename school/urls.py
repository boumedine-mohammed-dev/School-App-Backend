from django.urls import path,include
from .views import ProgramViewSet,EventViewSet,TeacherViewSet,TestimonialViewSet,StudentViewSet,GradeViewSet,ReviewViewSet,FeedbackUserViewSet,UserViewSet,ProfileViewSet,SubjectViewSet
from rest_framework.routers import DefaultRouter
from .views import ping
router=DefaultRouter()
router.register("programs",ProgramViewSet)
router.register("events",EventViewSet)
router.register("teacher",TeacherViewSet)
router.register("testimonials",TestimonialViewSet)
router.register("students",StudentViewSet)
router.register("grades",GradeViewSet)
router.register("reviews",ReviewViewSet)
router.register("FeedbackUser",FeedbackUserViewSet)
router.register("users",UserViewSet)
router.register("profiles",ProfileViewSet)
router.register("subjects",SubjectViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('ping/', ping),
]