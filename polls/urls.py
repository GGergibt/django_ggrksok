from django.urls import path

from . import views

# urlpatterns = [path("", views.render_something.as_view(), name="home")]
urlpatterns = [
    path("", views.home_page, name="home"),
    path("checkbox/checkbox/", views.get_file, name="link"),
    path("checkbox/", views.form_post, name="checkbox"),
    path("link", views.app_download, name="eckbox"),
    path("login/", views.login_page, name="login_page"),
    path("registration/", views.registration.as_view(), name="registration"),
    path("show_profiles", views.return_stored_profiles, name="show_profiles"),
]
