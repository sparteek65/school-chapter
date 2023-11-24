from django.contrib import admin
from .models import (Class,Chapter,Topic,Keyword,McqOption,FOMcq,
                     UserAnswer, ExamPapers, CaseStudies, CheatSheet,
                     FOMcqUserResponse)
# Register your models here.

admin.site.register(Class)
admin.site.register(Chapter)
admin.site.register(Keyword)
admin.site.register(Topic)

class McqAdmin(admin.ModelAdmin):
    list_display=('topic','question','answer')
    search_fields=('topic__name','topic__number','question')

class FOMcqUserResponseAdmin(admin.ModelAdmin):
    list_display=('user','topic','fomcq','fomcq_answer')
    # search_fields=('topic__name','topic__number','question')

admin.site.register(FOMcq,McqAdmin)
# admin.site.register(UserAnswer)
admin.site.register(ExamPapers)
admin.site.register(CaseStudies)
admin.site.register(CheatSheet)
admin.site.register(FOMcqUserResponse,FOMcqUserResponseAdmin)
