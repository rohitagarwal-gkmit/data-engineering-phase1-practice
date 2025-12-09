"""
URL configuration for apidemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from apidemo.schemas.add import AddRequest, AddResponse

api = NinjaAPI()


@api.post("/add", response=AddResponse)
def add(request, payload: AddRequest):
    """Adds two integers and returns the result.
    Args:
        request: The HTTP request object.
        payload (AddRequest): The request payload containing two integers 'a' and 'b'.
    Returns:
        AddResponse: The response containing the sum of 'a' and 'b'.
    """
    return {"result": payload.a + payload.b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
