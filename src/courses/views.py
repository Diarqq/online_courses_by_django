from django.shortcuts import render


def main_page(request):
    return render(request,'courses/course_list.html')


def course_detail_view(request):
    return render(request,'courses/course_detail.html')