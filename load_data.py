import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import Chel, Programma, Otziv, Stranica, Proverks

def load_data():
    Otziv.objects.all().delete()
    Programma.objects.all().delete()
    Chel.objects.all().delete()
    Stranica.objects.all().delete()
    Proverks.objects.all().delete()

    director, _ = Chel.objects.get_or_create(
        fio="Каткова С.В.",
        mesto="glava",
        pochta="skatkova@hse.ru",
        telefon="Академический руководитель",
        foto="assets/images/IMG_4792.PNG"
    )

    manager, _ = Chel.objects.get_or_create(
        fio="Санакова Т.Ю.",
        mesto="glava",
        pochta="tsanakova@hse.ru",
        telefon="Менеджер программы",
        foto="assets/images/IMG_4790.JPG"
    )

    Chel.objects.get_or_create(
        fio="Тихонов Елизавета Витальевна",
        mesto="avtor",
        pochta="elvitikhonov@edu.hse.ru",
        telefon="+79632985909",
        foto="assets/images/IMG_7597.jpg"
    )

    Chel.objects.get_or_create(
        fio="Германова Мария",
        mesto="stydent",
        pochta="magermanova@edu.hse.ru",
        telefon="+7 (967) 471-49-69",
        foto="assets/images/IMG_4817.PNG"
    )

    Chel.objects.get_or_create(
        fio="Шаповалова Елизавета",
        mesto="stydent",
        pochta="ershapovalova@edu.hse.ru",
        telefon="+7 (926) 121-03-33",
        foto="assets/images/IMG_4816.PNG"
    )

    prog, _ = Programma.objects.get_or_create(
        nazvamie="Реклама и связи с общественностью",
        opisanie="Программа готовит универсальных специалистов по коммуникациям за счёт интеграции дисциплин.",
        rukovoditel=director,
        menedjer=manager
    )

    Otziv.objects.get_or_create(kyrs=prog, nik="Елизавета Т.", tekst="Программа дает отличную базу в сфере коммуникаций.", ocenks=10)
    Otziv.objects.get_or_create(kyrs=prog, nik="Мария Г.", tekst="Интересные курсы по медиапланированию.", ocenks=9)

    Proverks.objects.create(
        imya="Проверка посещаемости", 
        info="Плановая проверка", 
        kogda=datetime.date.today(), 
        ststus="Завершено" 
    )
    Proverks.objects.create(
        imya="Аттестация", 
        info="Проверка знаний", 
        kogda=datetime.date.today() + datetime.timedelta(days=7), 
        ststus="В процессе"
    )

    Stranica.objects.get_or_create(
        skidka="media", 
        zagolovok="Медиа", 
        kontent="Изучение принципов работы современных медиа и стратегий продвижения в цифровой среде."
    )
    Stranica.objects.get_or_create(
        skidka="branding", 
        zagolovok="Брендинг", 
        kontent="Разработка визуальной и смысловой идентичности компаний и продуктов."
    )


if __name__ == '__main__':
    load_data()
