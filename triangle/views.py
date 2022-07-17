from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from triangle.forms import GetForm, PersonForm
from triangle.models import Person


def get_form(request):
    gip = None
    if 'submit' in request.GET:
        _get_form = GetForm(request.GET)
        if _get_form.is_valid():
            catet1 = _get_form.cleaned_data['catet1']
            catet2 = _get_form.cleaned_data['catet2']
            gip = round(((catet1 ** 2 + catet2 ** 2) ** 0.5), 3)

    else:
        _get_form = GetForm()
    return render(request,
                  'triangle/index.html',
                  {
                      'get_form': _get_form,
                      'gip': gip,
                  }
                  )


def person_create_form(request):
    if request.method == 'POST':
        person_form = PersonForm(data=request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('triangle:person-list')
    else:
        person_form = PersonForm()
    return render(
        request,
        "triangle/person_form.html",
        {
            'person_form': person_form
        }
    )


def person_update_form(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person_form = PersonForm(data=request.POST, instance=person)
        if person_form.is_valid():
            person_form.save()
            return redirect('triangle:person-list')
    else:
        person_form = PersonForm(instance=person)
    return render(
        request,
        "triangle/person_update_form.html",
        {
            'person_form': person_form,
            'person': person,
        }
    )


class PersonIndexView(generic.ListView):
    template_name = 'triangle/person_list.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()
