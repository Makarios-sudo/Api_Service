from django.urls import path
from .views import Lecture_ViewSet, Profile_ViewSet

urlpatterns = [
    path("lectures", Lecture_ViewSet.as_view({
        "get":"list",
        "post":"create",
    })),

    path("lectures/<str:pk>", Lecture_ViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "delete":"destroy"
    }) ),

    path("profiles", Profile_ViewSet.as_view({
        "get":"list",
        "post":"create",
    })),

    path("profiles/<str:pk>", Profile_ViewSet.as_view({
        "get":"retrieve",
        "put":"update"
        }))
]

