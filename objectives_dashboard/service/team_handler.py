


class TeamHandler:
    def __init__(self):
        pass

    def get_teams(self, payload):
        return {
            "data": [
                {
                    "lead": "alex",
                    "objectives": 10,
                    "no_of_employees": 2
                },
                {
                    "lead": "sales",
                    "objectives": 10,
                    "no_of_employees": 2
                }
            ]
        }