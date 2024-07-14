from django import forms
from web_app.models import PartnershipRequest,Subscriber
class PartnershipRequestForm(forms.ModelForm):
    agent = forms.CharField(max_length=255,required=False)
    market_entry = forms.CharField(max_length=255,required=False)
    others = forms.CharField(max_length=255,required=False)

    class Meta:
        model = PartnershipRequest
        fields = ['institute_name','address','contact_person','contact_person','contact_person','title','email','phone_no','message']

    def clean(self):
        cleaned_data = super().clean()
        agent = cleaned_data.get('agent')
        market_entry = cleaned_data.get('market_entry')
        others = cleaned_data.get('others')

        combined_value = f"{agent} , {market_entry}, {agent}"
        cleaned_data['interested_service'] = combined_value

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.interested_service = self.cleaned_data['interested_service']
        if commit:
            instance.save()
        return instance

class CombinedDataForm(forms.ModelForm):


    def clean(self):
        cleaned_data = super().clean()
        field1 = cleaned_data.get('field1')
        field2 = cleaned_data.get('field2')
        field3 = cleaned_data.get('field3')

        if field1 and field2 and field3:
            combined_value = f"{field1} {field2} {field3}"
            cleaned_data['combined_field'] = combined_value

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.combined_field = self.cleaned_data['combined_field']
        if commit:
            instance.save()
        return instance

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name','email']