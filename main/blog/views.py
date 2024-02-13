from django.shortcuts import render
from blog.models import Info , Expertise , Links , Education, Skills, Sertificate , Portfolio
from blog.forms import ContactForm
from django.db.models.query import QuerySet
from django.views.generic import TemplateView
from django.http import HttpResponse

def home(request):
    port = Portfolio.objects.all().order_by('-pk')
    cert = Sertificate.objects.all().order_by('pk')
    skil = Skills.objects.all().order_by('pk')
    edu = Education.objects.all().order_by('-name')[:]
    links = Links.objects.all().order_by('-name')[:]
    expert = Expertise.objects.all().order_by('-name')[:3]
    infos = Info.objects.all().order_by('-name')[:]
    context = {
        "port": port,
        "cert": cert,
        "skil": skil ,
        "edu" : edu ,
        "social" : links,
        "information": infos,
        "expertise": expert,

    }
    

    return render(request, 'index.html', context)


class ContactPageView(TemplateView):
    template_name = 'contact.html'
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Bog'langaniz uchun tasahkkur!")

        context = {
            'form': form
        }

        return render(request, 'contact.html', context)