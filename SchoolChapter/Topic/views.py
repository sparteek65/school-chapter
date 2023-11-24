from django.shortcuts import render
from Dashboard.models import Topic
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.http import HttpResponseNotAllowed
from django.db.models import Q
import json
from Dashboard.models import McqOption,UserAnswer,FOMcqUserResponse,FOMcq
# Create your views here.

def topic(request):
    topic_no=request.GET.get("n")
    if not topic_no:
        return render(request,'topic.html')
    else:
        topic=get_object_or_404(Topic,number=topic_no)

        return render(request,'topic.html',context={"topic":topic})
    
def mcq(request):
    topic_number= request.GET.get("topic_number")
    if not topic_number:
        return False
    topic=get_object_or_404(Topic,number=topic_number)
    return render(request,'fomcq.html',context={"topic":topic})

 

def search_everything(request):
    search_query = request.GET.get("q")
    if not search_query:
        return JsonResponse(data={[]})
    else:
        search_results= Topic.objects.filter(Q(name__in=search_query)|Q(number=search_query)|Q(description__in=search_query))
        print(search_results)
        return JsonResponse(search_results)

def mcq_submittion(request):
    if request.method=="POST":
        options = json.loads(request.body)
        for i in options:
            option = get_object_or_404(McqOption,id=i["option_id"])
            checked = i["checked"]
            user_answer,created=UserAnswer.objects.get_or_create(user=request.user,marked_correct=checked,option=option)
        return JsonResponse(data={"details":"MCQ Submitted Successfuly"})
    else:
        return HttpResponseNotAllowed(["POST"])

def fomcq_submittion(request):
    if request.method=="POST":
        mcq_responses = json.loads(request.body)
        for mcq_response in mcq_responses:
            fomcq = get_object_or_404(FOMcq,mcq_id=mcq_response["id"])
            fomcq_answer=mcq_response["number"]

            already_submitted_check = FOMcqUserResponse.objects.filter(user=request.user,
                                             fomcq=fomcq,
                                            topic = fomcq.topic)
            
            if already_submitted_check.count()==0:
                user_answer,created=FOMcqUserResponse.objects.get_or_create(user=request.user,
                                                                            fomcq=fomcq,
                                                                            topic = fomcq.topic,
                                                                            fomcq_answer=fomcq_answer)

        return JsonResponse(data={"details":"MCQ Submitted Successfuly"})
    else:
        return HttpResponseNotAllowed(["POST"])