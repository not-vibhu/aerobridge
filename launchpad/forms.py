from registry.models import Person, Address, Operator, Aircraft, Manufacturer, Firmware, Contact, Pilot, Engine, Activity
from digitalsky_provider.models import DigitalSkyLog
from gcs_operations.models import FlightOperation, FlightLog, FlightPlan, FlightPermission, Transaction
from pki_framework.models import AerobridgeCredential
from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

KEY_ENVIRONMENT = ((0, _('DIGITAL SKY OPERATOR')),(1, _('DIGITAL SKY MANUFACTURER')),(2, _('DIGITAL SKY PILOT')),(3, _('RFM')),(4, _('OTHER')),)

TOKEN_TYPE= ((0, _('PUBLIC_KEY')),(1, _('PRIVATE_KEY')),(2, _('AUTHENTICATION TOKEN')),(3, _('RFM KEY')),(4, _('OTHER')),)

# books/forms.py
class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        
class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class OperatorCreateForm(forms.ModelForm):
    class Meta:
        model = Operator
        exclude = ('expiration',)

class AircraftCreateForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        exclude = ('is_registered','type_certificate','esn',)

class ManufacturerCreateForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class FirmwareCreateForm(forms.ModelForm):
    class Meta:
        model = Firmware
        fields = '__all__'

class FlightPlanCreateForm(forms.ModelForm):
    class Meta:
        model = FlightPlan
        fields = '__all__'

class FlightPermissionCreateForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #    super(FlightPermissionCreateForm, self).__init__(*args, **kwargs)
    #    self.fields['is_successful'].widget.attrs['disabled'] = True
    #    self.fields['artefact'].widget.attrs['disabled'] = True

    class Meta:
        model = FlightPermission
        fields = ('operation',)
        

class FlightLogCreateForm(forms.ModelForm):
    class Meta:
        model = FlightLog
        fields = ('operation','raw_log', 'signed_log',)
        

class FlightOperationCreateForm(forms.ModelForm):
    class Meta:
        model = FlightOperation
        fields = '__all__'


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PilotCreateForm(forms.ModelForm):
    class Meta:
        model = Pilot
        fields = '__all__'

class DigitalSkyLogCreateForm(forms.ModelForm):
    class Meta:
        model = DigitalSkyLog
        fields = '__all__'

class DigitalSkyTransactionCreateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class EngineCreateForm(forms.ModelForm):
    class Meta:
        model = Engine
        fields = '__all__'
        

class ActivityCreateForm(forms.ModelForm):
    class Meta:
        model = Activity
        # exclude = ('is_created',)
        fields = '__all__'
        
class TokenCreateForm(forms.ModelForm):
    class Meta:
        model = AerobridgeCredential
        fields = '__all__'
        
class CutsomTokenCreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    token_type = forms.IntegerField(widget=forms.Select(choices=TOKEN_TYPE),
    )
    association = forms.IntegerField(widget=forms.Select(choices=KEY_ENVIRONMENT),
    )
    token = forms.CharField(widget = forms.TextInput())