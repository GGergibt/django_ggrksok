from django.urls import path

from . import views

# urlpatterns = [path("", views.render_something.as_view(), name="home")]
urlpatterns = [
    path("", views.page.as_view(), name="home"),
    path("checkbox/checkbox/", views.get_file, name="link"),
    path("checkbox/", views.form_post, name="checkbox"),
    path("link", views.app_download, name="eckbox"),
]
