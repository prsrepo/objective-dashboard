from django.http import JsonResponse
from django.views import View
from .service.objective_handler import ObjectiveHandler
from .service.department_handler import DepartmentHandler
from .service.team_handler import TeamHandler

# from .forms import MyForm


class ObjectivesSummary(View):
    def get(self, request):
        response = ObjectiveHandler().get_object_summary()
        return JsonResponse(response)


class Departments(View):
    def get(self, request):
        response = DepartmentHandler().get_departments()
        return JsonResponse(response)


class Teams(View):
    def post(self, request):
        response = TeamHandler().get_teams(request.data)
        return JsonResponse(response)

