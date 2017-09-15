from django.conf.urls import url
import views

urlpatterns = [
    url(r'^', views.send_email, name="send_email"),
]