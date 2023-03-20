from django.db import models


class Sector(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=200, verbose_name='Sektor nomi',
                            help_text='Sektor nomini kiriting')
    beg_price = models.CharField(blank=False, default=0, help_text='Sektorning boshlang\'ich narxini kiriting',
                                 verbose_name='Boshlang\'ich narx', max_length=50)
    end_price = models.CharField(blank=False, default=0, help_text='Sektorning ohirgi narxini kiriting',
                                 verbose_name='Ohirgi narx', max_length=50)
    quantity = models.PositiveIntegerField(verbose_name='Qatorlar soni', help_text='Qator sonini kiriting')
    image = models.ImageField(verbose_name='Rasim')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sektorlar"
        verbose_name_plural = "Sektorlar"


class Row(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nomi', help_text='Qator nomini kiriting')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, verbose_name='Sektor', help_text='Qator sektorini tanlang')
    quantity = models.PositiveIntegerField(verbose_name='Joylar soni', help_text='Joylar sonini kiriting')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.sector.name + " " + self.name + "-qator"

    class Meta:
        verbose_name = "Qatorlar"
        verbose_name_plural = "Qatorlar"


class Place(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nomi', help_text='Joy nomini kiriting')
    row = models.ForeignKey(Row, on_delete=models.CASCADE, verbose_name='Sektor', help_text='Joy qatorini tanlang')
    status = models.BooleanField(default=True, verbose_name='Holati')
    price = models.CharField(blank=False, default=0, help_text='Joyning narxini kiriting', verbose_name='narx', max_length=50)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Joylar"
        verbose_name_plural = "Joylar"


class User(models.Model):
    user_name = models.CharField(max_length=200, verbose_name='Ism', null=True)
    tg_id = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Telegram id')
    user_phone = models.CharField(max_length=20, unique=True, verbose_name='Raqam', null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return str(self.tg_id)

    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"


class Order(models.Model):
    pay_choice_option = [
        ('Click', 'click'),
        ('Payme', 'payme'),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Xaridor')
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, verbose_name='Joy', null=True)
    pay_type = models.CharField(choices=pay_choice_option, max_length=20, verbose_name='To\'lov turi')
    total_price = models.CharField(max_length=50, verbose_name='Umumiy narx')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.user.user_name

    class Meta:
        verbose_name = "Buyurtmalar"
        verbose_name_plural = "Buyurtmalar"


class AboutUs(models.Model):
    text = models.TextField(verbose_name="Umma forum haqida")
    update_date = models.DateTimeField(auto_now=True, verbose_name='Ohirgi martta o\'zgartirilgan sana')

    class Meta:
        verbose_name = 'Umma forum haqida'
        verbose_name_plural = 'Umma forum haqida'


class Calls(models.Model):
    phone = models.CharField(max_length=100, verbose_name='Aloqa uchun raqamlar')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    class Meta:
        verbose_name = 'Bog\'lanish uchun'
        verbose_name_plural = 'Bog\'lanish uchun'
