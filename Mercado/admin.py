from django.contrib import admin
from Mercado.models import mall, tienda, producto

# Register your models here.

class mallAdmin(admin.ModelAdmin):
    list_display = ('nombre','ubicacion')
    search_fields = ('nombre',)

class tiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre','mall')
    search_fields = ('nombre',)

class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio','tienda')
    search_fields = ('nombre',)

admin.site.register(mall, mallAdmin)
admin.site.register(tienda, tiendaAdmin)
admin.site.register(producto, productoAdmin)