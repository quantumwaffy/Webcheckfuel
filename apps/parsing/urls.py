from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="parsing"), path("upload-files", views.upload, name="upload_files")]
