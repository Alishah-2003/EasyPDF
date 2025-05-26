from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import uuid

class PDFUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=350, blank=True)
    file_uploaded = models.FileField(upload_to='pdfs/', validators=[FileExtensionValidator(['pdf'])])
    upload_time = models.DateTimeField(auto_now_add=True)

class SharePDF(models.Model):
    pdf = models.OneToOneField(PDFUpload, on_delete=models.CASCADE, related_name='sharepdf')
    link = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentPDF(models.Model):
    pdf = models.ForeignKey(PDFUpload, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    commenter = models.CharField(max_length=300, blank=True)


