from django import forms
from .models import Complaint, Comment

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'category', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...'}),
        }
        labels = {
            'text': '', 
        }

class ComplaintSatisfactionForm(forms.ModelForm):
    satisfied = forms.ChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        widget=forms.RadioSelect,
        required=True,
        label="Were you satisfied with the resolution?"
    )
    class Meta:
        model = Complaint
        fields = ['satisfied']

