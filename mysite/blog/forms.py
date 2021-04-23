from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        # isko hmne Post model se connect  kr dia
        fields = ('author', 'title', 'text')
        # given fields edit kr skte hum

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent '})

        }
        # ye shyd css editing krne ke liye hote widgets


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        # isko hmne Comment model s connect kr dia
        fields = ('author', 'text')
        # jo jo fields edit kr skte
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
