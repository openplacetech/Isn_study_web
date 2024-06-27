from django import forms
from web_app.models import PartnershipRequest
class PartnershipRequestForm(forms.ModelForm):
    class Meta:
        model = PartnershipRequest
        fields = ['institute_name','address','contact_person','contact_person','contact_person','title','email','phone_no','interested_service','message']
