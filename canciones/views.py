from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import CancionForm
from .services import song_service

CANCIONES_POR_PAGINA = 5

# Create your views here.
def index(request):
    busqueda = request.GET.get('q', '').strip()
    canciones = song_service.obtener_todas(busqueda)

    paginador = Paginator(canciones, CANCIONES_POR_PAGINA)
    pagina = paginador.get_page(request.GET.get('page', ''))
    return render(request, 'index.html', {
        'pagina': pagina,
        'busqueda': busqueda,
    })

def create(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            song_service.crear_cancion(form.cleaned_data)
            messages.success(request, 'Cancion agregada correctamente')
            return redirect('index')
    else:
        form = CancionForm()
    return render(request, 'canciones_form.html', {
        'form': form,
        'titulo': 'Agregar cancion',
    })

def update(request, id):
    cancion = song_service.obtener_por_id(id)

    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            song_service.actualizar_cancion(id, form.cleaned_data)
            messages.success(request, 'Cancion actualizada correctamente')
            return redirect('index')
    else:
        form = CancionForm(instance=cancion)

    return render(request, 'canciones_form.html', {
        'form': form,
        'titulo': 'Editar cancion',
    })

@require_POST
def delete(request, id):
    song_service.eliminar_cancion(id)
    messages.success(request, 'Cancion eliminada correctamente')
    return redirect('index')










