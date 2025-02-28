from django.shortcuts import render, redirect,get_object_or_404
from .models import Course, CoursePart,CourseTopic,TopicDocument
from .forms import CoursePartForm, CourseTopicForm, TopicDocumentForm, CourseCreateForm
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy


#COURSE VIEWS
def main_page(request):
    courses = Course.objects.all()
    return render(request,'courses/course_list.html',{'course_list':courses})

@login_required()
def course_detail_view(request, pk):
    if request.method == 'GET':
        course = Course.objects.get(id=pk)
        #courseparts = CoursePart.objects.filter(course_id=pk)
        course_parts = CoursePart.objects.filter(course_id=pk).prefetch_related(
            Prefetch('topics', queryset=CourseTopic.objects.all(), to_attr='prefetched_topics')
        )

        return render(request,'courses/course_detail.html',{'course':course,'course_parts':course_parts})

@login_required()
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
@login_required()
def course_update_view(request,pk):
    course = get_object_or_404(Course,id=pk)
    if request.method == "GET":
        form = CourseCreateForm(instance=course)
        return render(request, 'courses/course_form.html', {'form': form})
    elif request.method == 'POST':
        form = CourseCreateForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
        return redirect('course_detail',pk)


@login_required()
def course_delete_view(request,pk):
    course = get_object_or_404(Course, id=pk)
    print(course)
    if request.method == 'GET':
        return render(request,'courses/course_confirm_delete.html',{'course':course})
    elif request.method == 'POST':

        course.delete()
        print('q'*5)
        return redirect('course_list')




#COURSE PARTS VIEWS



@login_required()
def course_part_list_view(request):
    courseparts = CoursePart.objects.all()
    return render(request,'courses/coursepart_list.html',{'coursepart_list':courseparts})

@login_required()
def course_part_detail_view(request,pk):
    if request.method == 'GET':
        courseparts = CoursePart.objects.get(id=pk)
        return render(request, 'courses/coursepart_detail.html', { 'coursepart': courseparts})

@login_required()
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

@login_required()
def course_part_create_with_course_view(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    if request.method == 'GET':
        form = CoursePartForm(instance=course)
        return render(request, 'courses/coursepart_form_with_course.html', {'form': form,'course_id':course_id})
    elif request.method == 'POST':
        form = CoursePartForm(request.POST)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('course_detail',course_id)

@login_required()
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

@login_required()
def course_part_delete_view(request,pk):
    coursepart = get_object_or_404(CoursePart, id=pk)
    if request.method == 'GET':
        return render(request, 'courses/coursepart_confirm_delete.html', {'coursepart': coursepart})
    elif request.method == 'POST':
        coursepart.delete()
        return redirect('coursepart_list')





#COURSE TOPICS VIEWS



@login_required()
def course_topic_list_view(request):
    coursetopics = CourseTopic.objects.all()
    return render(request,'courses/coursetopic_list.html',{'coursetopic_list':coursetopics})

@login_required()
def course_topic_detail_view(request,pk):
    if request.method == 'GET':
        coursetopic = CourseTopic.objects.get(id=pk)
        return render(request, 'courses/coursetopic_detail.html', {'coursetopic': coursetopic})

@login_required()
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

@login_required()
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

@login_required()
def course_topic_update_view(request,pk):
    coursetopic = get_object_or_404(CourseTopic, id=pk)
    if request.method == 'GET':
        form = CourseTopicForm(instance=coursetopic)
        return render(request, 'courses/coursetopic_form.html', {'form': form})
    elif request.method == 'POST':
        form = CourseTopicForm(request.POST,instance=coursetopic)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('coursetopic_list')

@login_required()
def course_topic_delete_view(request,pk):
    coursetopic = get_object_or_404(CourseTopic, id=pk)
    if request.method == 'GET':
        return render(request, 'courses/coursetopic_confirm_delete.html', {'coursetopic': coursetopic})
    elif request.method == 'POST':
        coursetopic.delete()
        return redirect('coursetopic_list')

#COURSE DOCUMENTS VIEWS

@login_required()
def document_list(request):
    docs = TopicDocument.objects.all()
    if request.method == 'GET':
        form = TopicDocumentForm()
    if request.method == 'POST':
        form = TopicDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print('q')
            form.save()
    return render(request, 'document/document_list.html', {'form': form,'documents':docs})


@login_required()
def update_document(request,document_id):
    document = get_object_or_404(TopicDocument,id=document_id)
    if request.method == 'GET':
        form = TopicDocumentForm(instance=document)
        return render(request, 'document/update_document.html', {'form': form})
    elif request.method == 'POST':
        form = TopicDocumentForm(request.POST,request.FILES,instance=document)
        if form.is_valid():
            print('q')
            form.save()
        return redirect('document_list')

@login_required()
def delete_document(request,pk):
    document = get_object_or_404(TopicDocument, id=pk)
    if request.method == 'GET':
        return render(request, 'document/confirm_delete.html', {'document': document})
    elif request.method == 'POST':
        document.delete()
        return redirect('document_list')