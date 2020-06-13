from django import forms

class OrderCreateForm(forms.Form):
    start_date = forms.DateField()
    duration = forms.IntegerField()

    def clean_duration(self):
        duration = self.cleaned_data['duration']        
        if duration < 0:
            raise forms.ValidationError("Duration must be positive")
        return duration
