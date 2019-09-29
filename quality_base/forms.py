from django import forms
from quality_base.models import Amber
from quality_base.models import Document

class AmberForm(forms.ModelForm):
    class Meta:
        model = Amber
        fields = ('controller','serial_number','inspection_1','inspection_2','inspection_3','inspection_4',
                  'inspection_5','inspection_6','comments')





class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description' , 'document',)
