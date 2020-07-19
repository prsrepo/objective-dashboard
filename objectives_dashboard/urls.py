from django.urls import path
from .views import ObjectivesSummary, Departments, Teams

urlpatterns = [
    path('objective_summary/', ObjectivesSummary.as_view()),
    path('departments/', Departments.as_view()),
    path('teams/', Teams.as_view()),
]


