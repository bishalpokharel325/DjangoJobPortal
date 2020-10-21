from django.contrib import admin

# Register your models here.
from .models import Candidate


@admin.register(Candidate)
class AdminCandidate(admin.ModelAdmin):
    list_display = ['name', 'relocate']
    date_hierarchy = "date"
    search_fields = ['name', 'age', 'salary_expectation', 'gender']
