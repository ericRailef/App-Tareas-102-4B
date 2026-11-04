from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Mascota
from .forms import MascotaForm


def inicio(request):
    total = Mascota.objects.count()
    return render(request, 'mascotas/inicio.html', {'total': total})


@login_required
def listar_mascotas(request):
    mascotas = Mascota.objects.all().order_by('nombre')
    return render(request, 'mascotas/listado.html', {'mascotas': mascotas})


@login_required
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota registrada correctamente.')
            return redirect('listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'mascotas/crear.html', {'form': form})


@login_required
def detalle_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    return render(request, 'mascotas/detalle.html', {'mascota': mascota})


@login_required
def editar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota modificada correctamente.')
            return redirect('listar_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascotas/editar.html', {'form': form, 'mascota': mascota})


@login_required
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    if request.method == 'POST':
        mascota.delete()
        messages.success(request, 'Mascota eliminada correctamente.')
        return redirect('listar_mascotas')
    return render(request, 'mascotas/eliminar.html', {'mascota': mascota})
