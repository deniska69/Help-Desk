from django.db import models
from django.core.urlresolvers import reverse

# Таблица "Лаборатории"
class Lab(models.Model):
    dp = models.ForeignKey('Employees', blank=True, null=True, on_delete=models.SET_NULL) # ID Зав.Лаб
    abb = models.CharField(max_length=250)                      # Аббревиатура названия
    title = models.CharField(max_length=250)                    # Название
    lab_logo = models.FileField()                               # Расположение логотипа на сервер

    def get_absolute_url(self):
        return reverse('ivc:detail', kwargs={'pk': self.pk})

    # Для отображения в админке:
    def __str__(self):
        return self.abb

# Таблица "Заявки"
class App(models.Model):
    em = models.ForeignKey('Employees', blank=True, null=True, on_delete=models.SET_NULL)  # ID Подающего
    tp = models.ForeignKey('Type_App', blank=True, null=True, on_delete=models.SET_NULL)    # ID Тип заявки
    cr = models.ForeignKey('Classroom', blank=True, null=True, on_delete=models.SET_NULL)   # ID Аудитории

    date1 = models.DateField()                              # Дата регистрации заявки
    st = models.ForeignKey('Status')        # ID Статуса
    date2 = models.DateField(blank=True, null=True)         # Дата выполнения заявки

    note = models.CharField(blank=True, null=True, max_length=250)                 # Доп. информация по заявке
    username = models.CharField(blank=True, null=True, max_length=250)

    # Для отображения в админке:
    def __str__(self):
        return self.tp.lb.abb + ' - ' + self.tp.title + ' | Статус: ' + self.st.title

# Таблица "Статус"
class Status(models.Model):
    title = models.CharField(max_length=250)  # Название

    # Для отображения в админке:
    def __str__(self):
        return self.title

# Таблица "Корпуса"
class Housing(models.Model):
    no_hs = models.CharField(max_length=10)     # Номер корпуса
    adds = models.CharField(max_length=250)     # Адрес корпуса
    fac = models.CharField(max_length=250)      # Факультеты
    title = models.CharField(max_length=250)    # Название

    # Для отображения в админке:
    def __str__(self):
        return '№ ' + self.no_hs + ' - ' + self.adds + ' - ' + self.title

# Таблица "Аудитории"
class Classroom(models.Model):
    hs = models.ForeignKey(Housing, on_delete=models.CASCADE)   # ID Корпуса
    no_cr = models.CharField(max_length=10)                     # Номер аудитории
    title = models.CharField(max_length=250)                    # Название

    # Для отображения в админке:
    def __str__(self):
        return '№ ' + self.no_cr + ' - ' + self.title

# Таблица "Подразделения"
class Subdivision(models.Model):
    dp = models.ForeignKey('Employees', blank=True, null=True, on_delete=models.SET_NULL)  # ID Начальника
    abb = models.CharField(max_length=250)                       # Аббревиатура названия
    title = models.CharField(max_length=250)                     # Название

    # Для отображения в админке:
    def __str__(self):
        return self.abb + ' - ' + self.title

# Таблица "Типы_заявок"
class Type_App(models.Model):
    lb = models.ForeignKey(Lab, on_delete=models.CASCADE)   # ID Лаборатории
    title = models.CharField(max_length=250)                # Название

    # Для отображения в админке:
    def __str__(self):
        return self.lb.abb + ' - ' + self.title

# Таблица "Сотрудники"
class Employees(models.Model):
    sd = models.ForeignKey(Subdivision, on_delete=models.CASCADE)   # ID Подразделения
    cr = models.ForeignKey(Classroom, on_delete=models.CASCADE)     # ID Аудитории
    lb = models.ForeignKey(Lab, blank=True, null=True, on_delete=models.SET_NULL)   # ID Лаборатории
    fio = models.CharField(max_length=250)                          # ФИО
    email = models.CharField(max_length=250)                        # Email
    intel = models.CharField(max_length=250)                        # Внутренний телефон
    mbtel = models.CharField(max_length=250)                        # Мобильный телефон
    func = models.CharField(max_length=250)                         # Должность

    username = models.CharField(blank=True, null=True, max_length=250)
    avatar = models.FileField(blank=True, null=True)

    # Для отображения в админке:
    def __str__(self):
        return self.sd.abb + ' - ' + self.fio