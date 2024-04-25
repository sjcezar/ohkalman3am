from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]

