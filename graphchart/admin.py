from django.contrib import admin
from graphchart.models import Reading

class ReadingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['temperature']}),
        ('Time information', {'fields' :['reading_time']}),

        ]

    list_display =('temperature', 'reading_time', 'was_read_recently')
    list_filter = ['reading_time']
    
admin.site.register(Reading, ReadingAdmin)
# Register your models here.
