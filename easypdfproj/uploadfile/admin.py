from django.contrib import admin
from .models import PDFUpload, SharePDF, CommentPDF

# Register your models here.
admin.site.register(PDFUpload)
admin.site.register(SharePDF)
admin.site.register(CommentPDF)
