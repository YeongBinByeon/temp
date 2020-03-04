from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)

    def __str__(self):
        return self.todo

    def save(self, force_insert=False, using=None, update_fields=None):
        if not self.name:
            self.name = "홍길동"
        super().save()

class MainActionStatics(models.Model):
    date = models.DateField('date')
    tv_search_title = models.IntegerField('tv_search_title')
    tv_unknown_search = models.IntegerField('tv_unknown_search')
    tv_open_search = models.IntegerField('tv_open_search')
    tv_play_title = models.IntegerField('tv_play_title')
    
    def __str__(self):
        return self.todo