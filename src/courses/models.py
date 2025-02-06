from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        abstract = True



    def delete(self, using=None, keep_parents=False):
        # Установить время удаления вместо удаления строки
        self.deleted_at = now()
        self.save()

    @property
    def is_deleted(self):
        return self.deleted_at is not None



class Course(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


#NOT MINE > REWORK

class CoursePart(BaseModel):
    course = models.ForeignKey(Course, related_name='parts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(default=None)

    @property
    def topic_count(self):
        return self.topics.count()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'title'],
                condition=models.Q(deleted_at__isnull=True),
                name='unique_course_part'
            )
        ]

    def __str__(self):
        return f"{self.course.title}-{self.title}"


class CourseTopic(BaseModel):
    part =  models.ForeignKey(CoursePart, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(default=None)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['part', 'title'],
                condition=models.Q(deleted_at__isnull=True),
                name='unique_course_topic'
            )
        ]

    def __str__(self):
        return f"{self.part.title}-{self.title}"


class TopicDocument(BaseModel):
    topic = models.ForeignKey(CourseTopic, related_name='documents', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='topic_documents/')

    def __str__(self):
        return self.name


class TopicText(BaseModel):
    topic = models.ForeignKey(CourseTopic, related_name='texts', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Text for {self.topic.title}"
