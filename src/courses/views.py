from django.shortcuts import render, redirect,get_object_or_404
from .models import Course, CoursePart,CourseTopic,TopicDocument
from .forms import CoursePartForm, CourseTopicForm, TopicDocumentForm, CourseCreateForm
from django.db.models import Prefetch

#COURSE VIEWS
def main_page(request):
    courses = Course.objects.all()
    return render(request,'courses/course_list.html',{'course_list':courses})


def course_detail_view(request, pk):
    if request.method == 'GET':
        course = Course.objects.get(id=pk)
        #courseparts = CoursePart.objects.filter(course_id=pk)
        course_parts = CoursePart.objects.filter(course_id=pk).prefetch_related(
            Prefetch('topics', queryset=CourseTopic.objects.all(), to_attr='prefetched_topics')
        )

        return render(request,'courses/course_detail.html',{'course':course,'course_parts':course_parts})


def course_create_view(request):
    if request.method == 'GET':
        form = CourseCreateForm()
        return render(request, 'courses/course_form.html', {'form': form})
    elif request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('course_list')

def course_update_view(request,pk):
    course = get_object_or_404(Course,id=pk)
    if request.method == "GET":
        print('GET '*7)
        form = CourseCreateForm(initial={'course':course,'title':course.title,'description':course.description})
        return render(request, 'courses/course_form.html', {'form': form})
    elif request.method == 'POST':
        print('Post ' * 7)
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            print('IS VALID '*7)
            form.save()
        return redirect('course_detail',pk)

def course_delete_view(request):
    pass




#COURSE PARTS VIEWS




def course_part_list_view(request):
    courseparts = CoursePart.objects.all()
    return render(request,'courses/coursepart_list.html',{'coursepart_list':courseparts})
def course_part_detail_view(request,pk):
    if request.method == 'GET':
        courseparts = CoursePart.objects.get(id=pk)
        return render(request, 'courses/coursepart_detail.html', { 'coursepart': courseparts})


def course_part_create_view(request):
    if request.method == 'GET':
        form = CoursePartForm()
        return render(request, 'courses/coursepart_form.html', {'form': form})
    elif request.method == 'POST':
        form = CoursePartForm(request.POST)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('coursepart_list')
def course_part_create_with_course_view(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    if request.method == 'GET':
        form = CoursePartForm(initial={'course':course})
        return render(request, 'courses/coursepart_form.html', {'form': form})
    elif request.method == 'POST':
        form = CoursePartForm(request.POST)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('course_detail',course_id)
def course_part_update_view(request,pk):
    coursepart = get_object_or_404(CoursePart, id=pk)
    if request.method == 'GET':
        form = CoursePartForm(instance=coursepart)
        return render(request, 'courses/coursepart_form.html', {'form': form})
    elif request.method == 'POST':
        form = CoursePartForm(request.POST,instance=coursepart)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('coursepart_detail', pk)
def course_part_delete_view(request):
    pass





#COURSE TOPICS VIEWS




def course_topic_list_view(request):
    coursetopics = CourseTopic.objects.all()
    return render(request,'courses/coursetopic_list.html',{'coursetopic_list':coursetopics})
def course_topic_detail_view(request,pk):
    if request.method == 'GET':
        coursetopic = CourseTopic.objects.get(id=pk)
        return render(request, 'courses/coursetopic_detail.html', {'coursetopic': coursetopic})
def course_topic_create_with_course_part_view(request,part_id):
    coursepart = get_object_or_404(CoursePart, id=part_id)
    if request.method == 'GET':
        form = CourseTopicForm(initial={'part':coursepart})
        return render(request, 'courses/coursetopic_form.html', {'form': form})
    elif request.method == 'POST':
        form = CourseTopicForm(request.POST,initial={'part':coursepart})
        if form.is_valid():
            print('q')
            form.save()
        return redirect('coursetopic_list')
def course_topic_create_view(request):
    if request.method == 'GET':
        form = CourseTopicForm()
        return render(request, 'courses/coursetopic_form.html', {'form': form})
    elif request.method == 'POST':
        form = CourseTopicForm(request.POST)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('coursetopic_list')
def course_topic_update_view(request):
    pass
def course_topic_delete_view(request):
    pass

#COURSE DOCUMENTS VIEWS


def document_list(request):
    docs = TopicDocument.objects.all()
    return render(request, 'document/document_list.html',{'documents':docs})

def update_document(request):
    if request.method == 'GET':
        form = TopicDocumentForm()
        return render(request, 'courses/update_document.html', {'form': form})
    elif request.method == 'POST':
        form = TopicDocumentForm(request.POST)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('document_list')
def delete_document(request):
    pass