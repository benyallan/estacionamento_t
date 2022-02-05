from django.urls import path, include
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movRotativos,
    lista_movMensalistas,
    lista_Mensalistas,
    pessoa_novo,
    veiculo_novo,
    movRot_novo,
    mensalista_novo,
    movMens_novo,
    pessoa_update,
    veiculo_update,
    movRotativos_update,
    movMensalistas_update,
    mensalista_update,
    pessoa_delete,
    veiculo_delete,
    movRot_delete,
    movMens_delete,
    mensalista_delete,
    Pdf,
    )

urlpatterns = [
    path('', home, name='core_home'),
    
    # CRUD de Pessoas
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo', pessoa_novo, name='core_pessoa_novo'),
    path('pessoas-update/<int:id>', pessoa_update, name='core_pessoa_update'),
    path('pessoas-delete/<int:id>', pessoa_delete, name='core_delete_pessoa'),
    
    # CRUD de Veículos
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo', veiculo_novo, name='core_veiculo_novo'),
    path(
            'veiculos-update/<int:id>', 
            veiculo_update, 
            name='core_veiculo_update'
        ),
    path(
            'veiculos-delete/<int:id>', 
            veiculo_delete, 
            name='core_delete_veiculo'
        ),
    
    # CRUD de Movimento rotativo
    path('mov-rot-list', lista_movRotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo', movRot_novo, name='core_movrot_novo'),
    path(
            'mov-rot-update/<int:id>', 
            movRotativos_update, 
            name='core_movrotativos_update'
        ),
    path(
            'mov-rot-delete/<int:id>', 
            movRot_delete, 
            name='core_delete_movrot'
        ),
    
    # CRUD de Movimento de mensalistas
    path(
            'mov-movmens-list', lista_movMensalistas, 
            name='core_lista_movmensalistas'
        ),
    path(
        'mov-movmens-novo', movMens_novo, name='core_movmens_novo'),
    path(
            'mov-mens-update/<int:id>', 
            movMensalistas_update, 
            name='core_movmensalistas_update'
        ),
    path(
            'mov-mens-delete/<int:id>', 
            movMens_delete, 
            name='core_delete_movmens'
        ),
    
    # CRUD de Mensalistas
    path('mensalistas', lista_Mensalistas, name='core_mensalistas'),
    path('mensalistas-novo', mensalista_novo, name='core_mensalista_novo'),
    path(
            'mensalistas-update/<int:id>', 
            mensalista_update, 
            name='core_mensalista_update'
        ),
    path(
            'mensalistas-delete/<int:id>', 
            mensalista_delete, 
            name='core_delete_mensalista'
        ),
    
    
    # Relatório PDF
    path(
            'relatorio', 
            Pdf.as_view(), 
            name='relatorio_pdf'
        ),
]
