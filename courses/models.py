from django.db import models


class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name: 'Course'
        verbose_name_plural: 'Courses'
        ordering = ['id']

    def __str__(self):
        return self.title


class Assessment(Base):
    id_course = models.ForeignKey(Course, related_name='assessments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    assessment = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name: 'Assessment'
        verbose_name_plural: 'Assessments'
        unique_together = ['email', 'id_course']
        ordering = ['id']

    def __str__(self):
        return f'{self.name} avaliou o curso {self.id_course} com nota {self.assessment}'
