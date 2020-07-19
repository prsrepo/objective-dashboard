from ..models import Objectives, Department, Keyresults
from django.http import JsonResponse


class ObjectiveHandler:
    def __init__(self):
        """
        default constructor
        """
        pass

    def get_summary(self):
        """
        This method is used to get summary of the Objectives
        :return:
        """
        start_time = Department.objects.earliest('date_of_inauguration').date_of_inauguration
        completed_objectives = 0
        objectives = Objectives.objects.all()
        for objective in objectives:
            if not len(Keyresults.objects.filter(objective=objective, status='done')):
                completed_objectives += 1
        return JsonResponse({
            "data": {
                "all_objectives": len(objectives),
                "completed_objectives": completed_objectives,
                "start_time": str(start_time)
            }
        })

