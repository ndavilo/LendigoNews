from django import forms
from .models import Post, Comment



class PostForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields 	= ('title', 'by', 'body', 'attached_image')

		widgets 	= {
			'title'			:	forms.TextInput(attrs={'class': 'form-control'}),
			'by'			:	forms.TextInput(attrs={'class': 'form-control'}),
			'body'			:	forms.Textarea(attrs={'class': 'form-control'}),

		} 

class EditForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields 	= ('title', 'body')

		widgets 	= {
			'title'			:	forms.TextInput(attrs={'class': 'form-control'}),
			'body'			:	forms.Textarea(attrs={'class': 'form-control'}),

		} 

class AddCommentForm(forms.ModelForm):
	class Meta:
		model 		=	Comment
		fields 		=	('body','by')
		widgets 	=	{
				'body'			:	forms.Textarea(attrs={'class': 'form-control'}),
				'by'			:	forms.TextInput(attrs={'class': 'form-control'}),
		}

class EditCommentForm(forms.ModelForm):
	class Meta:
		model 		=	Comment
		fields 		=	('body',)
		widgets 	=	{
				'body'			:	forms.Textarea(attrs={'class': 'form-control'})
		}

		