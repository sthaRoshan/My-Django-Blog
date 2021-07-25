from .models import Post
from django import forms


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "overview", "body_text", "thumbnail", "publish", "categories"]