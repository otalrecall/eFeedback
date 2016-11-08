from django.contrib import admin

from .models import Check, CheckList, Task, Solution, State

admin.site.register(Task)
admin.site.register(Check)
admin.site.register(Solution)
admin.site.register(CheckList)
admin.site.register(State)