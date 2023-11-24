from django import template
from ..models import McqOption,Mcq,Class, Chapter,Topic,FOMcq,FOMcqUserResponse
from typing import Tuple,Optional
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


register = template.Library()

@register.filter()
def get_user_marked_correct(option:McqOption,user):
    return option.user_answer.filter(user=user).first()

@register.filter()
def is_mcq_submitted(mcq:Mcq,user)->Tuple[Optional[bool]]:
    user_answer_correct_set=list()
    options=mcq.options.all()
    user_ans_count=0

    box_shadow_red="box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 0px 3px rgba(255, 0, 0, 1);"
    box_shadow_green="box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 0px 3px rgba(0, 255, 0, 1);"
    box_shadow_grey="box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 0px 3px rgba(0, 0, 0, 1);"

    for option in options:
        user_ans=option.user_answer.filter(user=user).first()
        if user_ans:
            user_ans_count+=1
            user_answer_correct_set.append(option.correct==user_ans.marked_correct)
    
    
    if user_ans_count==0:
        # never attempt
        return (None,box_shadow_grey)
    
    elif all(user_answer_correct_set):
        # submitted correctly
        # submitted corrrectly (show answer,show_badge)
        return (True,box_shadow_green)
    
    elif len(options)!=user_ans_count:
        # half attempt
        return (None,box_shadow_red)
    # Incorrect submitttion
    return (False,box_shadow_red)
            
@register.filter()
def chapters_of_class(c):
    return Chapter.objects.filter(of_class=c)

@register.filter()
def topic_of_chapter(c):
    return Topic.objects.filter(chapter=c)

@register.filter()
def topic_tiles(topic_number):
    topic_obj= get_object_or_404(Topic,number=topic_number)
    
    return {"fomcq":topic_obj.fomcq_set.count()>0,
            "cheatsheet":topic_obj.cheatsheet_set.count()>0,
            "casestudies":topic_obj.casestudies_set.count()>0,
            "exampapers":topic_obj.exampapers_set.count()>0,
            }
    
@register.filter()
def fomcqs_for_topic_number(topic_number):
    topic_obj= get_object_or_404(Topic,number=topic_number)
    
    return topic_obj.fomcq_set.all()

@register.filter()
def is_fomcq_submitted(fomcq:FOMcq,user:User)->Tuple[Optional[bool]]:
    if user.is_anonymous:
        return False
    user_mcq_response = FOMcqUserResponse.objects.filter(user=user,
                                                         fomcq=fomcq).last()
    return user_mcq_response
    