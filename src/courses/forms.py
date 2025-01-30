from  django import forms
from .models import TopicDocument, CourseTopic, Course, CoursePart




class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','description']
        labels= {
            'title':'Назва',
            'description':'Апісанне',
        }

class CoursePartForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Select a Course",
        required=True
    )

    class Meta:
        model = CoursePart
        fields = ['course', 'title']


class CourseTopicForm(forms.ModelForm):
    part = forms.ModelChoiceField(
        queryset=CoursePart.objects.all(),
        empty_label="Select a Course Part",
        required=True
    )

    class Meta:
        model = CourseTopic
        fields = ['part', 'title', ]


class TopicDocumentForm(forms.ModelForm):
    topic = forms.ModelChoiceField(
        queryset=CourseTopic.objects.all(),
        empty_label="Select a Topic",
        required = True
    )

    class Meta:
        model = TopicDocument
        fields = ['name', 'file', 'topic']
