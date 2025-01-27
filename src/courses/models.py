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