from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# from .forms import MyForm

class ObjectivesSummary(View):
    # form_class = MyForm
    def get(self, request):
        return HttpResponse({
            "data": {
                "objectives": 80,
                "completed": 60,
                "start_time": "15-06-2020"
            }
        })

class Departments(View):
    def get(self, request):
        return HttpResponse({
            "data": [
                {
                    "name": "sales",
                    "objectives": 10,
                    "no_of_employees": 2
                },
                {
                    "name": "sales",
                    "objectives": 10,
                    "no_of_employees": 2
                }
            ]
        })


class Teams(View):
    def post(self, request):
        return HttpResponse({
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
        })