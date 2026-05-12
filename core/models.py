from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Chel(models.Model):
    ROLI = [('stydent', 'Студент'), ('prepod', 'Преподаватель'), ('glava', 'Начальник'), ('avtor', 'Автор')]
    fio = models.CharField(max_length=100)
    pochta = models.EmailField()
    telefon = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='photos/', null=True, blank=True)
    mesto = models.CharField(max_length=20, choices=ROLI)
    def __str__(self): return self.fio

class Programma(models.Model):
    nazvamie = models.CharField(max_length=200)
    opisanie = models.TextField()
    rukovoditel = models.ForeignKey(Chel, related_name='progi_dir', on_delete=models.SET_NULL, null=True)
    menedjer = models.ForeignKey(Chel, related_name='progi_man', on_delete=models.SET_NULL, null=True)
    def __str__(self): return self.nazvamie

class Otziv(models.Model):
    kyrs = models.ForeignKey(Programma, related_name='otzivi', on_delete=models.CASCADE, null=True, blank=True)
    nik = models.CharField(max_length=100)
    tekst = models.TextField()
    ocenks = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    data_sozdaniya = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.nik

class Stranica(models.Model):
    skidka = models.SlugField(unique=True)
    zagolovok = models.CharField(max_length=200)
    kontent = models.TextField()
    def __str__(self): return self.zagolovok

class Proverks(models.Model):
    imya = models.CharField(max_length=200)
    info = models.TextField()
    kogda = models.DateField()
    ststus = models.CharField(max_length=50)
    def __str__(self): return self.imya
