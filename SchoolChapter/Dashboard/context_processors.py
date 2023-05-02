from .models import Class


def classes(request):
    classes = Class.objects.all()
    return {'classes': classes}


def classes_proc(request):
    response = list()
    classes = Class.objects.all()
    for class_ in classes:
        chapters = list()
        for chapter in class_.chapter_set.all():
            chapters.append({"chapter": chapter,
                             "topics": chapter.topic_set.all(),
                             })
        response.append({"class": class_,
                         "chapters": chapters})
    return {"classes_proc": response}


def class_exam_papers(request):
    response = list()
    classes = Class.objects.all()
    for class_ in classes:

        response.append({"class": class_,
                         "papers": class_.exampaper_class.all()})

    return {"class_papers": response}

def case_studies(request):
    response = list()
    classes = Class.objects.all()
    for class_ in classes:

        response.append({"class": class_,
                         "case_study": class_.case_studies_class.all()})

    return {"case_studies": response}