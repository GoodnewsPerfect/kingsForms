from django.shortcuts import render
from .forms import Title, FullName, KingsChat, ActiveKcId, Zone, Church, Attendance, Certification, Badge, Feedback, \
    Observation
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Title(request.POST)
        form1 = FullName(request.POST)
        form2 = KingsChat(request.POST)
        form3 = ActiveKcId(request.POST)
        form4 = Zone(request.POST)
        form5 = Church(request.POST)
        form6 = Attendance(request.POST)
        form7 = Certification(request.POST)
        form8 = Badge(request.POST)
        form9 = Feedback(request.POST)
        form10 = Observation(request.POST)
        print(request.POST)
        if form.is_valid() or form1.is_valid() or form2.is_valid() or form3.is_valid() or form4.is_valid(
        ) or form5.is_valid() or form6.is_valid() or form7.is_valid() or form8.is_valid() or form9.is_valid(
        ) or form10.is_valid():
            return HttpResponse(
                "<center style='background-color: lightgrey'><h1>Thank you for filling this form. </h1></center>")

    form = Title()
    form1 = FullName()
    form2 = KingsChat()
    form3 = ActiveKcId()
    form4 = Zone()
    form5 = Church()
    form6 = Attendance()
    form7 = Certification()
    form8 = Badge()
    form9 = Feedback()
    form10 = Observation()
    return render(request, 'kingsForms/home.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3,
                                                    'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7,
                                                    'form8': form8, 'form9': form9, 'form10': form10})
