from django.forms import ModelForm
from Collage.models import *

class AnswerSheetForm(ModelForm):
    class Meta:
        model = AnswerSheet
        fields = "__all__"
        
        
class StudentResultSheetForm(ModelForm):
    class Meta:
        model = StudentResultSheet
        fields = "__all__"