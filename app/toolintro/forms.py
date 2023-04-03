from django import forms
from .models import ToolReviewRating

class ToolReviewForm(forms.ModelForm):
    class Meta:
        model = ToolReviewRating
        fields = ['subject', 'review', 'rating']
