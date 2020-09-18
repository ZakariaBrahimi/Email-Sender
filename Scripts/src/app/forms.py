from django import forms



class SubscribeForm(forms.Form):
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"input100", 'type':"text", 'name':"subject", 'placeholder':"Enter The Subject"}))
    to_email = forms.EmailField(widget=forms.TextInput(attrs={'class':"input100", 'type':"text", 'name':"to_email", 'placeholder':"Enter sender email"}))
    body = forms.CharField(widget=forms.Textarea    (attrs={'class':"input100", 'name':"message", 'placeholder':"Your Message..."}))
    attachments = forms.FileInput()