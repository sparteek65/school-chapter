from django import template
from ..models import McqOption,Mcq,Class, Chapter,Topic
from typing import Tuple,Optional
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