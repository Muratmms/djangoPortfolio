from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    CONTENT_TYPES = (
        ('article', 'Article'),
        ('feature', 'Feature'),
        ('gallery', 'Gallery'),
        ("video", "Video"),
        ("slider", "Slider"),
        ("image", "Image"),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(default="null",null=True, blank=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    content_type = models.CharField(max_length=100, choices=CONTENT_TYPES, default='article')
    extraData = models.JSONField(blank=True, null=True) 

    def __str__(self):
        return self.title
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    