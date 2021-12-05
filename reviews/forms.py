from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """
    class Meta:
        model = Review
        fields = ['title', 'comment', 'rating']

        exclude = (
            'user',
            'product',
            'date_added',
        )

    labels = {
        'rating': 'Rating',
    }

    def __init__(self, *args, **kwargs):
        """ Insert placeholders for form """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'comment': 'Comment',
        }

        # Add placeholders and classes to input fields

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = 'border-black rounded-1'
