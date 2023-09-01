from django.contrib import admin

from .models import Categoria, Marca, Acessório, Cor, Veiculo
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessório)
admin.site.register(Cor)
admin.site.register(Veiculo)


