from django.contrib import admin
from .models import Company, Device, Subscriber, Subscription


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 1


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'condition')
    list_filter = ('company',)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')
    list_filter = ('company', 'devices')
    inlines = [SubscriptionInline]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')
    list_filter = ('employees',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
