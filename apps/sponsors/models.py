from django.db import models


# Create your models here.


class Sponsors(models.Model):
    SPONSOR_STATUS = [
        ('new', 'Yangi'),
        ('moderation', 'Moderatsiyada'),
        ('approved', 'Tasdiqlangan'),
        ('declained', 'Bekor qilingan'),
    ]

    SPONSOR_PAYMENT_TYPE = [
        ('cash', 'Naqd Pul'),
        ('transaction', "Pul o'tkazmalari")
    ]

    SPONSOR_TYPE = [
        ('entity', 'Yuridik shaxs'),
        ('individual', 'Jismoniy shaxs'),
    ]

    full_name = models.CharField(max_length=150, verbose_name='Спонсоры')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    sponsor_type = models.CharField(max_length=100, choices=SPONSOR_TYPE, default='entity', verbose_name="Тип спонсора")
    sponsorship_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Спонсировано')
    sponsorship_spent_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Потрачено')
    payment_type = models.CharField(max_length=50, choices=SPONSOR_PAYMENT_TYPE, default="cash", verbose_name='Тип оплаты')
    company_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название компании')
    status = models.CharField(max_length=150, choices=SPONSOR_STATUS, verbose_name='Статус')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = "- Спонсор"
        verbose_name_plural = "- Спонсоры"

    def __str__(self):
        return self.full_name
