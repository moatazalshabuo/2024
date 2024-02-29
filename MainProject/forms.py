from django import forms
from .models import *
class BesicDataForm(forms.ModelForm):
    
    class Meta:
        model = BesicData
        fields = ['title','from_date','to_date','about']
        

class OrganizersForm(forms.ModelForm):
    
    class Meta:
        model = Organizers
        fields = '__all__'
        

class ShepherdsForm(forms.ModelForm):
    
    class Meta:
        model = Shepherds
        fields = '__all__'
        
        
class ScheduleForm(forms.ModelForm):
    
    class Meta:
        model = Schedule
        fields = '__all__'
        
        
class SpeakersForm(forms.ModelForm):
    
    class Meta:
        model = Speakers
        fields = '__all__'
        
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        
        
class GustisForm(forms.ModelForm):
    class Meta:
        model = Gustis
        fields = "__all__"
        
class CloudsForm(forms.ModelForm):
    class Meta:
        model = Clouds
        fields = "__all__"
        
class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = "__all__"