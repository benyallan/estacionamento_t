from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.http import HttpResponse
import csv
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



@login_required
def home(request):
    return render(request, 'core/index.html')


# CRUD de Pessoas
@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required
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


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})



# CRUD de Veículos
@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
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


@login_required
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
@login_required
def lista_movRotativos(request):
    mov_rot = movRotativo.objects.all()
    form = MovRotForm()
    data = {'mov_rot': mov_rot, 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)


@login_required
def movRot_novo(request):
    form = MovRotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


@login_required
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


@login_required
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
@login_required
def lista_movMensalistas(request):
    mov_mens = movMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mens': mov_mens, 'form': form}
    return render(request, 'core/lista_movmensalistas.html', data)


@login_required
def movMens_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


@login_required
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


@login_required
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
@login_required
def lista_Mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)


@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mensalistas')


@login_required
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


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_mensalistas')
    else:
        return render(
                request, 'core/delete_confirm.html', {'obj': mensalista}
            )


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


# Relatório PDF
class Pdf(View):

    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', params, 'relatorio_veiculos')
    

# Relatório CSV
class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response