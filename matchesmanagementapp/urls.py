from django.urls import path
from . import views

urlpatterns = [
    path('matchesmanagement/<int:id>',views.MatchView.as_view()),
    path('matchesmanagement',views.MatchView.as_view())

    
    
]