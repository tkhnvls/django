from django.contrib import admin
from .models import Chel, Programma, Otziv, Stranica, Proverks

@admin.register(Chel)
class ChelAdmin(admin.ModelAdmin):
    list_display = ('fio', 'mesto', 'pochta')
    list_filter = ('mesto',)

@admin.register(Programma)
class ProgrammaAdmin(admin.ModelAdmin):
    list_display = ('nazvamie', 'rukovoditel')

@admin.register(Otziv)
class OtzivAdmin(admin.ModelAdmin):
    list_display = ('nik', 'ocenks', 'data_sozdaniya')
    list_filter = ('ocenks',)

@admin.register(Stranica)
class StranicaAdmin(admin.ModelAdmin):
    list_display = ('zagolovok', 'skidka')

@admin.register(Proverks)
class ProverksAdmin(admin.ModelAdmin):
    list_display = ('imya', 'kogda', 'ststus')
    list_filter = ('ststus',)
