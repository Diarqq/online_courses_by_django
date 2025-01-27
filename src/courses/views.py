from django.shortcuts import render



#COURSE VIEWS
def main_page(request):
    return render(request,'courses/course_list.html')


def course_detail_view(request):
    return render(request,'courses/course_detail.html')

def course_create_view(request):
    pass

def course_update_view(request):
    pass


def course_delete_view(request):
    pass

#COURSE PARTS VIEWS


def course_part_list_view(request):
    pass
def course_part_detail_view(request):
    pass
def course_part_create_view(request):
    pass
def course_part_create_with_course_view(request):
    pass
def course_part_update_view(request):
    pass
def course_part_delete_view(request):
    pass


#COURSE TOPICS VIEWS

def course_topic_list_view(request):
    pass
def course_topic_detail_view(request):
    pass
def course_topic_create_with_course_part_view(request):
    pass
def course_topic_create_view(request):
    pass
def course_topic_update_view(request):
    pass
def course_topic_delete_view(request):
    pass

#COURSE DOCUMENTS VIEWS


def document_list(request):
    pass
def update_document(request):
    pass
def delete_document(request):
    pass