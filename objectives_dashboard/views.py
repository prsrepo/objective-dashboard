from django.views import View
from .service.objective_handler import ObjectiveHandler
from .service.department_handler import DepartmentHandler
from .service.team_handler import TeamHandler
from json import loads


class ObjectivesSummary(View):
    def get(self, request):
        return ObjectiveHandler().get_summary()


class Departments(View):
    def get(self, request):
        return DepartmentHandler().get_departments()


class Teams(View):
    def post(self, request):
        return TeamHandler().get_teams(loads(request.body))

