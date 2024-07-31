from django.contrib import admin
from .models import( Profile , 
                    Project,
                    ProjectImage ,
                     Experience)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_user_name','get_first_name','get_last_name','bio', 'summary']

    def get_first_name(self,obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self,obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'
    
    def get_user_name(self, obj):
        return obj.user.username
    get_user_name.short_description = 'Username'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title' , 'company', 'start_date','end_date']