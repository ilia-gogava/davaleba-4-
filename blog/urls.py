from django.urls import path include # new
from .views import BlogListView
from django.contrib import admin
from .views import BlogListView, BlogDetailView # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"), # new
    path("", include("blog.urls")), # new
    path("", BlogListView.as_view(), name="home"),
]