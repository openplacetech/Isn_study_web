from django.contrib import admin
from web_app.models import PartnershipRequest,PrivacyPolicy,Insights,ISNTeam,CurrierOpportunities
# Register your models here.
@admin.register(PartnershipRequest)
class PartnershipRequestAdmin(admin.ModelAdmin):
    list_display = ('institute_name', 'address', 'contact_person','title','email','interested_service','created_at')
    search_fields = ('institute_name', 'email' , 'contact_person')
    list_filter = ('created_at', 'updated_at')
    list_editable = ()

@admin.register(Insights)
class InsightsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','category','created_at', 'updated_at')
    search_fields = ('title', 'slug', 'category')
    list_filter = ('created_at', 'updated_at')

@admin.register(ISNTeam)
class ISNTeamAdmin(admin.ModelAdmin):
    list_display = ('full_name','designation','created_at', 'updated_at')
    search_fields = ('full_name','designation')
    list_filter = ('created_at','updated_at')

@admin.register(CurrierOpportunities)
class CurrierOpportunitiesAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'category', 'job_mode', 'job_type','job_status')
    search_fields = ('job_title', 'job_status','job_mode', 'job_type')
    list_filter = ('created_at', 'updated_at')

admin.site.register(PrivacyPolicy)