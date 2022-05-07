from django.urls import path
from .views import Profile_List, Profile_Details, Profile_UpdateView, Profile_DeleteView


urlpatterns = [
    path("profiles/", Profile_List.as_view()),
    path("profile/<str:pk>", Profile_Details.as_view),
    path("profile/<str:pk>", Profile_UpdateView.as_view()),
    path("profile/<str:pk>", Profile_DeleteView.as_view()),



]