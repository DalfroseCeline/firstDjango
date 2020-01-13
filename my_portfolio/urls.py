from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutt, name='about'),
    path('experience', views.experience, name='experience'),
    path('education', views.education, name='education'),
    path('skills', views.skills, name='skills'),
    path('interests', views.interests, name='interests'),
    path('family', views.family, name='family'),
]

