from django.urls import path
from . import views

urlpatterns = [
    # /polls/
    path('', views.index, name="index"),
    # /polls/5/
    path('<int:question_id>/', views.details, name="question_detail"),
    # /polls/5/results/
    path('<int:question_id>/results/', views.results,  name="question_results"),
    # /polls/5/votes/
    path('<int:question_id>/votes/', views.votes, name="question_votes"),
]
