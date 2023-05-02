from django.contrib import admin
from .models import Class,Chapter,Topic,Keyword,McqOption,Mcq,UserAnswer, ExamPapers, CaseStudies, CheatSheet
# Register your models here.

admin.site.register(Class)
admin.site.register(Chapter)
admin.site.register(Keyword)
admin.site.register(Topic)

class McqAdmin(admin.ModelAdmin):
    list_display=('topic','question','answer')
    search_fields=('topic__name','topic__number','question')

admin.site.register(Mcq,McqAdmin)
admin.site.register(McqOption)
admin.site.register(UserAnswer)
admin.site.register(ExamPapers)
admin.site.register(CaseStudies)
admin.site.register(CheatSheet)
