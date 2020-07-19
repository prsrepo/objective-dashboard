from objectives_dashboard.models import Department, Teams, Users, Objectives, Keyresults, UserTeamMappping
from datetime import datetime
import names
from random import randint, choice


"""
This scripts can be used to generate the data for application.

Process of data creation:

$ python manage.py shell

>>> from scripts.data import dump_data

>>> dump_data()

"""


departments = [
    {
        'department_id': 'sales',
        'name': "Sales",
        'location': 'Bangalore',
        'date_of_inauguration': datetime(2020, 1, 1)
    },
    {
        'department_id': 'engineering',
        'name': "Engineering",
        'location': 'Hyderabad',
        'date_of_inauguration': datetime(2020, 2, 1)
    },
    {
        'department_id': 'product',
        'name': "Product",
        'location': 'Chennai',
        'date_of_inauguration': datetime(2020, 3, 1)
    },
    {
        'department_id': 'customer_success',
        'name': "Customer Success",
        'location': 'Mumbai',
        'date_of_inauguration': datetime(2020, 4, 1)
    },
    {
        'department_id': 'hr_ops',
        'name': "HR Ops",
        'location': 'Mumbai',
        'date_of_inauguration': datetime(2020, 4, 1)
    },
    {
        'department_id': 'it',
        'name': "IT",
        'location': 'Mumbai',
        'date_of_inauguration': datetime(2020, 4, 1)
    },
    {
        'department_id': 'manufacturing',
        'name': "Manufacturing",
        'location': 'Mumbai',
        'date_of_inauguration': datetime(2020, 4, 1)
    },
    {
        'department_id': 'legal',
        'name': "Legal",
        'location': 'Mumbai',
        'date_of_inauguration': datetime(2020, 4, 1)
    }
]


def dump_data():
    for department in departments:
        Department.objects.create(**department)
        for team_index in range(5):
            team_id = department.get('department_id') + '_team_' + str(team_index)
            Teams.objects.create(**{
                'team_id': team_id,
                'department': Department.objects.get(department_id=department.get('department_id'))
            })
            for user_index in range(5):
                f_name = names.get_first_name()
                l_name = names.get_last_name()
                user_id = f_name.lower() + '_' + l_name.lower() + str(user_index)
                Users.objects.create(**{
                    'user_id': user_id,
                    'first_name': f_name,
                    'last_name': l_name,
                    'salary': randint(30000, 90000)
                })
                UserTeamMappping.objects.create(**{
                    'is_team_lead': True if user_index == 0 else False,
                    'user': Users.objects.get(user_id=user_id),
                    'team': Teams.objects.get(team_id=team_id)
                })
                for obj_i_id in range(5):
                    obj_id = user_id + '_obj_' + str(obj_i_id)
                    Objectives.objects.create(**{
                        'objective_id': obj_id,
                        'user': Users.objects.get(user_id=user_id),
                        'objective_text': obj_id + " objective text"
                    })
                    for kr_i_id in range(5):
                        kr_id = obj_id + '_kr_' + str(kr_i_id)
                        Keyresults.objects.create(**{
                            'keyresult_id': kr_id,
                            'objective': Objectives.objects.get(objective_id=obj_id),
                            'status': choice(['done', 'active']),
                            'due_date': datetime(2020, 1, 3)
                        })


