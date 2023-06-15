from django import forms


class LocationSubscribeForm(forms.Form):
    choices = [
        (1, "서울"),
        (2, "세종"),
        (3, "강릉"),
        (4, "제주"),
        (5, "부산"),
    ]
    checkbox_field = forms.MultipleChoiceField(
        
        choices=choices,
    )