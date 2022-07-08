from django.shortcuts import render

from triangle.forms import GetForm


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
