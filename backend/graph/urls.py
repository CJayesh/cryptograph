from django.urls import path

from . import views

urlpatterns = [
    path('', views.HistoricalData.as_view(), name='get_graph_data'),
]
