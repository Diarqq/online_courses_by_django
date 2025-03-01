from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Course view
    path("", views.main_page, name="course_list"),
    path("course_detail/<int:pk>/", views.course_detail_view, name="course_detail"),
    path("create/", views.course_create_view, name="course_create"),
    path("update/<int:pk>/", views.course_update_view, name="course_update"),
    path("delete/<int:pk>/", views.course_delete_view, name="course_delete"),
    # CoursePart views
    path("parts/", views.course_part_list_view, name="coursepart_list"),
    path(
        "parts/detail/<int:pk>/", views.course_part_detail_view, name="coursepart_detail"
    ),
    path("parts/create/", views.course_part_create_view, name="coursepart_create"),
    path(
        "parts/create/<int:course_id>/",
        views.course_part_create_with_course_view,
        name="coursepart_create_with_course",
    ),
    path(
        "parts/update/<int:pk>/", views.course_part_update_view, name="coursepart_update"
    ),
    path(
        "parts/delete/<int:pk>/", views.course_part_delete_view, name="coursepart_delete"
    ),
    # CourseTopic views
    path("topics/", views.course_topic_list_view, name="coursetopic_list"),
    path(
        "topics/detail/<int:pk>/",
        views.course_topic_detail_view,
        name="coursetopic_detail",
    ),
    path(
        "coursetopics/create/<int:part_id>/",
        views.course_topic_create_with_course_part_view,
        name="coursetopic_create_with_coursepart",
    ),
    path("topics/create/", views.course_topic_create_view, name="coursetopic_create"),
    path(
        "topics/update/<int:pk>/",
        views.course_topic_update_view,
        name="coursetopic_update",
    ),
    path(
        "topics/delete/<int:pk>/",
        views.course_topic_delete_view,
        name="coursetopic_delete",
    ),
    # CourseDocuments views
    path("document_list/", views.document_list, name="document_list"),
    path(
        "update_document/<int:document_id>", views.update_document, name="update_document"
    ),
    path(
        "delete_document/<int:document_id>", views.delete_document, name="delete_document"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
