from django.contrib import admin

# Register your models here.
from .models import Job


@admin.register(Job)
class AdminJob(admin.ModelAdmin):
    exclude = ['creator']

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creator=request.user)

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ['position_name', 'created_at', 'creator']
        else:
            return ['position_name', 'created_at']

    list_per_page = 10
    date_hierarchy = 'created_at'
    search_fields = ['position_name', 'description', 'created_at', 'salary']

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()
