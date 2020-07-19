from django.http import JsonResponse

from ..models import Teams, Department, UserTeamMappping, Objectives


class TeamHandler:
    def __init__(self):
        pass

    @staticmethod
    def ___validate_get_teams_payload(payload):
        if payload.get('department_id'):
            if type(payload.get('department_id')) == str:
                return True, None
            else:
                return False, "'department_id' should be a string"
        else:
            return False, "'department_id' is required"

    def get_teams(self, payload):
        is_valid, message = TeamHandler().___validate_get_teams_payload(payload)
        if is_valid:
            result = []
            teams = Teams.objects.filter(userteammappping__is_team_lead=True,
                                         department=Department.objects.get(department_id=payload.get('department_id')))
            for team in teams:
                user = UserTeamMappping.objects.get(is_team_lead=True, team=team).user
                lead_name = user.first_name + ' ' + user.last_name + "'s Team"
                user_in_team = UserTeamMappping.objects.filter(team=team)
                objectives = Objectives.objects.filter(user__in=[user_m.user for user_m in user_in_team])
                result.append({
                    "lead": lead_name,
                    "objectives": len(objectives),
                    "no_of_employees": len(user_in_team)
                })
            return JsonResponse({
                "data": result
            })
        else:
            return JsonResponse({"message": message}, status=400)

