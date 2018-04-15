from django.contrib import admin
from .models import *

class BgResultInline(admin.TabularInline):
    model = BgResult
    extra = 0

class BgResultAdmin(admin.ModelAdmin):
    list_display = [field.name for field  in BgResult._meta.fields]
    exclude = ["bg_index",]												#не отображает выбраное поле модели
    list_filter = ['bg_date', 'nickname']
    
    class Meta:
        model = BgResult

admin.site.register(BgResult, BgResultAdmin)





class MinimumAdmin(admin.ModelAdmin):
	list_display = ['force','minimum'] 									# отображает указаные поля модели 
	

	class Meta:
		model = Minimum



admin.site.register(Minimum, MinimumAdmin)

