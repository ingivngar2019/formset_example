from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, render, redirect, render
from django.template import RequestContext as ctx
from django.forms.models import inlineformset_factory

from .models import Receta, Ingrediente, Instruccion
from .forms import RecetaForm


def recetas(request):
    template_name = 'restaurant/recetas.html'
    recetas = Receta.objects.all()
    return render(request, template_name ,{
        'recetas': recetas
    })


def registro_edicion(request, receta_id=None):
    template_name = 'restaurant/registro-edicion.html'
    if receta_id:
        receta = Receta.objects.get(pk=receta_id)
    else:
        receta = Receta()

    IngredienteFormSet = inlineformset_factory(Receta, Ingrediente, extra=0, can_delete=True,fields=('descripcion',))
    InstruccionFormSet = inlineformset_factory(Receta, Instruccion, extra=0, can_delete=True,fields=('descripcion','numero'))

    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        ingredienteFormset = IngredienteFormSet(request.POST, instance=receta)
        instruccionFormset = InstruccionFormSet(request.POST, instance=receta)

        if form.is_valid() and ingredienteFormset.is_valid() and instruccionFormset.is_valid():
            form.save()
            ingredienteFormset.save()
            instruccionFormset.save()
            return redirect('lista')
    else:
        form = RecetaForm(instance=receta)
        ingredienteFormset = IngredienteFormSet(instance=receta)
        instruccionFormset = InstruccionFormSet(instance=receta)

    # return render('restaurant/registro-edicion.html', locals(),
    #     context_instance=ctx(request))
    return render(request, template_name ,locals())
