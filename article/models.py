from django.db import models
from django_editorjs import EditorJsField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = EditorJsField(
        verbose_name='Content',
        editorjs_config={
            "tools": {
                "Image": {
                    "config": {
                        "endpoints": {
                            "byFile": '/imageUpload/',
                            "byUrl": '/imageUpload/',
                        },
                        "additionalRequestHeaders": [{"Content-Type": 'multipart/form-data'}]
                    }
                },
                "Attaches": {
                    "config": {
                        "endpoint": '/fileUpload/'
                    }
                }
            }
        })
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    instagram = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True)
    mail = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.first_name


class AboutMe(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = EditorJsField(
        verbose_name='Content',
        editorjs_config={
            "tools": {
                "Image": {
                    "config": {
                        "endpoints": {
                            "byFile": '/imageUpload/',
                            "byUrl": '/imageUpload/',
                        },
                        "additionalRequestHeaders": [{"Content-Type": 'multipart/form-data'}]
                    }
                },
                "Attaches": {
                    "config": {
                        "endpoint": '/fileUpload/'
                    }
                }
            }
        })
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.first_name
