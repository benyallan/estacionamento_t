from django.contrib import admin
from .models import (
        Marca, Veiculo, Pessoa, Parametro, movRotativo, Mensalista, 
        movMensalista
    )

class movRotativoAdminAdmin(admin.ModelAdmin):

    list_display = (
        'checkin', 'checkout', 'total', 'veiculo', 'pago', 'horas_total'
    )
    
    
class movMensalistaAdmin(admin.ModelAdmin):

    list_display = ('mensalista', 'dt_pgto', 'total')
    
    
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(movRotativo, movRotativoAdminAdmin)
admin.site.register(Mensalista)
admin.site.register(movMensalista, movMensalistaAdmin)
