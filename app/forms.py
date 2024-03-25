from django import forms

from app.models import Entry, ActivityType


class LoginForm(forms.Form):
    token = forms.CharField(max_length=100, label='Token')


class signinForm(forms.Form):
    alias = forms.CharField(max_length=30, label='alias')

class NewGroup(forms.Form):
    name = forms.CharField(max_length=30, label='name')
    description = forms.CharField(max_length=30, label='description')

class NewActivityType(forms.Form):
    name = forms.CharField(max_length=30, label='name')

class NewEntry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        group = kwargs.pop('group', None)
        super().__init__(*args, **kwargs)
        if group:
            activity_types = ActivityType.objects.filter(group=group)
            choices = [(atype.id, atype.name) for atype in activity_types]
            self.fields['activityType'].choices = choices
        else:
            self.fields['activityType'].queryset = ActivityType.objects.none()  # No group specified, so set empty queryset

    class Meta:
        model = Entry
        fields = ['activityType', 'text']
        widgets = {
            'activityType': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }

class JoinGroupForm(forms.Form):
    group_id = forms.IntegerField(label='Group ID', required=True)