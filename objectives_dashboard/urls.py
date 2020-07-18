from django.urls import path
from .views import ObjectivesSummary

urlpatterns = [
    path('objective_summary/', ObjectivesSummary.as_view())
]

