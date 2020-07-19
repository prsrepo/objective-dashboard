from django.http import JsonResponse

from ..models import Department


class DepartmentHandler:
    def __init__(self):
        pass

    def get_departments(self):
        departments = Department.objects.all()
        return JsonResponse({
            "data": list(departments.values())
        })

