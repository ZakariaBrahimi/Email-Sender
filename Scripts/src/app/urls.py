from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'app'
urlpatterns = [
    url('', views.send_email, name='send_email'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)