from django import forms
from web_app.models import PartnershipRequest,Subscriber,InsightComments,ApplyForCareer
class PartnershipRequestForm(forms.ModelForm):
    agent = forms.CharField(max_length=255,required=False)
    market_entry = forms.CharField(max_length=255,required=False)
    others = forms.CharField(max_length=255,required=False)
    other_field=forms.CharField(max_length=255,required=False)

    class Meta:
        model = PartnershipRequest
        fields = ['institute_name','address','contact_person','title','email','phone_no','message']

    def clean(self):
        cleaned_data = super().clean()
        agent = cleaned_data.get('agent')
        market_entry = cleaned_data.get('market_entry')
        others = cleaned_data.get('others')
        if others:
            other_field = cleaned_data.get('other_field')
            others_field = other_field+" (Others)"
            cleaned_data['interested_service'] = others_field
        else:
            parts = [item for item in [agent, market_entry] if item]
            combined_value = ", ".join(parts)
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

class InsightCommentsForm(forms.ModelForm):
    class Meta:
        model = InsightComments
        fields = ['name','email','message']

class ApplyForCareerForm(forms.ModelForm):
    class Meta:
        model = ApplyForCareer
        fields = ['first_name','last_name','email','phone_number','contact_phone_type','other_job_consider',
                  'country','profile_link','expected_salary','resume','gender','veteran_status',
                  'race_ethnicity','disability','disability','legal_name','required_immigration_sponsorship','currency_type','pay_period',
                  'is_previously_employed','is_former_current_intern_or_contractor','receive_text_message','availability_or_notice_period']
