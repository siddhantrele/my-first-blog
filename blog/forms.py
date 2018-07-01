from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
		
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'placeholder': 'Write your title here!'})
        self.fields['title'].label=''

        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'rows': 15})
        self.fields['text'].widget.attrs.update({'placeholder': 'Write here!'})
        self.fields['text'].label=''

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
        	'text' : forms.Textarea(),
        	'author' : forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'rows': 3})
        self.fields['text'].widget.attrs.update({'placeholder': 'Write your comment here!'})
        self.fields['text'].label=''