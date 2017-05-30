from django.contrib import admin
from .models import Town, Reserved, Flat

class TownAdmin(admin.ModelAdmin):
    list_display = ['__str__']

class ReservedAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'isFree']
    list_filter = ['isFree', 'flatName', 'userName', 'beginDate', 'endDate']
    actions= ['set_free', 'set_busy']
    fields = ['beginDate', 'endDate', 'flatName', 'userName', 'isFree']

    def set_free(self, request, queryset):
        updated = queryset.update(isFree = True)
        if updated == 1:
            message = "1 date was" 
        else:
            message= "%s dates were" % updated
        self.message_user(request, "%s successfully set as free." % message)
    
    set_free.short_descripiton = "Mark selected dates as free"

    def set_busy(self, request, queryset):
        updated = queryset.update(isFree = False)
        if updated == 1:
            message = "1 date was" 
        else:
            message= "%s dates were" % updated 
        self.message_user(request, "%s successfully set as busy." % message)
   
    set_busy.short_descripiton = "Mark selected dates as busy"

class FlatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'canRent']
    list_filter = ['canRent', 'location']
    actions = ['set_open', 'set_busy']
    fields = ['flatName', 'location','openTime', 'openTimeEnd', 'canRent']

    def set_open(self, request, queryset):
        updated = queryset.update(canRent = True)
        if updated == 1:
            message = "1 Flat was" 
        else:
            message= "%s Flats were" % updated
        self.message_user(request, "%s successfully set as rentable." % message)
    set_open.short_descripiton = "Mark selected dates as rentable"

    def set_busy(self, request, queryset):
        updated = queryset.update(canRent = False)
        if updated == 1:
            message = "1 Flat was" 
        else:
            message= "%s Flats were" % updated
        self.message_user(request, "%s successfully set as busy." % message)
    set_busy.short_descripiton = "Mark selected flat as unRentable"
# Register your models here.

myModels = [ Town, Reserved, Flat ]
admin.site.register(Town, TownAdmin)
admin.site.register(Reserved, ReservedAdmin)
admin.site.register(Flat, FlatAdmin)

