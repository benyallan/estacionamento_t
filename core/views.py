from django.shortcuts import render, redirect
from .models import (
        Pessoa, 
        Veiculo,
        movRotativo,
        movMensalista,
        Mensalista,
    )
from .forms import (
        PessoaForm, 
        VeiculoForm, 
        MovRotForm,
        MensalistaForm,
        MovMensalistaForm
    )


def home(request):
    context = {'mensagem': 'Olá mundo!!!'}
    return render(request, 'core/index.html', context)


# CRUD de Pessoas
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


# CRUD de Veículos
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)
    
    
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(
                request, 'core/delete_confirm.html', {'obj': veiculo}
            )


# CRUD de Movimentos rotativos
def lista_movRotativos(request):
    mov_rot = movRotativo.objects.all()
    form = MovRotForm()
    data = {'mov_rot': mov_rot, 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)


def movRot_novo(request):
    form = MovRotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def movRotativos_update(request, id):
    data = {}
    mov_rotativo = movRotativo.objects.get(id=id)
    form = MovRotForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativos.html', data)


def movRot_delete(request, id):
    mov_rotativo = movRotativo.objects.get(id=id)
    
    if request.method == 'POST':
        mov_rotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(
                request, 'core/delete_confirm.html', {'obj': mov_rotativo}
            )


# CRUD de Movimento de mensalistas
def lista_movMensalistas(request):
    mov_mens = movMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mens': mov_mens, 'form': form}
    return render(request, 'core/lista_movmensalistas.html', data)


def movMens_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


def movMensalistas_update(request, id):
    data = {}
    mov_mensalista = movMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalistas.html', data)
    
    
def movMens_delete(request, id):
    mov_mens = movMensalista.objects.get(id=id)
    
    if request.method == 'POST':
        mov_mens.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(
                request, 'core/delete_confirm.html', {'obj': mov_mens}
            )


# CRUD de Mensalistas
def lista_Mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mensalistas')


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)
    
    
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_mensalistas')
    else:
        return render(
                request, 'core/delete_confirm.html', {'obj': mensalista}
            )