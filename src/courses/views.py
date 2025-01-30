from django.shortcuts import render, redirect
from .models import Course
from .forms import CoursePartForm, CourseTopicForm, TopicDocumentForm, CourseCreateForm


#COURSE VIEWS
def main_page(request):
    return render(request,'courses/course_list.html')


def course_detail_view(request):
    return render(request,'courses/course_detail.html')

def course_create_view(request):
    if request.method == 'GET':
        form = CourseCreateForm()
        test = 12345
        return render(request, 'courses/course_form.html', {'form': form,'test':test})
    elif request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('course_list')

def course_update_view(request):
    pass


def course_delete_view(request):
    pass

#COURSE PARTS VIEWS


def course_part_list_view(request):
    return render(request,'courses/coursepart_list.html')
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
    return render(request,'courses/coursetopic_list.html')
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
    return render(request, 'document/document_list.html')

def update_document(request):
    pass
def delete_document(request):
    pass