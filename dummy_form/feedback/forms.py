from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="You name",
#         max_length=100,
#         error_messages={
#             'required': 'you name must be filled',
#             "max_length": "The maximu length for name is 100 characters"
#         })
#     review_text = forms.CharField(label="Your feedback",
#                                   widget=forms.Textarea,
#                                   max_length=500)
#     rating = forms.IntegerField(max_value=5)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = "__all__"