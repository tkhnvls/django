from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count
from .models import Chel, Programma, Otziv, Stranica, Proverks
from .forms import OtzivForm

def dom(request): return render(request, 'core/home.html')

def ycheba(request):
    ya = Chel.objects.filter(mesto='avtor').first()
    proga = Programma.objects.first()
    gryppa = Chel.objects.filter(mesto='stydent')
    sort = request.GET.get('sort', '-data_sozdaniya')
    otzivi = Otziv.objects.all().order_by(sort)
    ball = otzivi.aggregate(Avg('ocenks'))['ocenks__avg']
    if request.method == 'POST':
        f = OtzivForm(request.POST)
        if f.is_valid():
            o = f.save(commit=False)
            o.kyrs = proga
            o.save()
            return redirect('education')
    else:
        f = OtzivForm()
    return render(request, 'core/education.html', {'ya': ya, 'proga': proga, 'gryppa': gryppa, 'otzivi': otzivi, 'forma': f, 'ball': ball})

def staty(request):
    spisok = Programma.objects.annotate(n=Count('otzivi'), a=Avg('otzivi__ocenks'))
    return render(request, 'core/task_1018.html', {'spisok': spisok})

def monitor(request):
    d = Proverks.objects.all().order_by(request.GET.get('sort', 'kogda'))
    return render(request, 'core/monitoring.html', {'dannie': d})

def info_str(request, slug):
    s = get_object_or_404(Stranica, skidka=slug)
    return render(request, 'core/page.html', {'obj': s})
