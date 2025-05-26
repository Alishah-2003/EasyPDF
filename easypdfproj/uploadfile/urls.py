from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard_view,name='dashboard'),
    path('viewallpdfs/',views.view_share_pdf, name='viewallpdfs'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('select_share/',views.select_share,name='select_share'),
    path('generate/<int:pdf_id>', views.generate_link, name="generate"),
    path('share_file/<uuid:link>',views.share_file,name="share_file")
    
]