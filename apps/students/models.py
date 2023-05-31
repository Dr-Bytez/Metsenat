from django.db import models

from apps.sponsors.models import Sponsors


# Create your models here.


class Students(models.Model):
    STUDENT_LEVEL_TYPE = [
        ('Bachelor', 'Bakalavr'),
        ('Master', "Magistr")
    ]

    full_name = models.CharField(max_length=150, verbose_name='Студент')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    student_level_type = models.CharField(max_length=50, choices=STUDENT_LEVEL_TYPE, verbose_name='Тип студента')
    university_name = models.CharField(max_length=255, verbose_name='Университет')
    student_need_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сумма контракта')
    student_get_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Получено для контракта')
    student_sponsors = models.ManyToManyField(Sponsors, verbose_name='Спонсор', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = "- Студент"
        verbose_name_plural = "- Студенты"

    def __str__(self):
        return self.full_name
