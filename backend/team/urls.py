from django.urls import path
from .views import api_root, team_member_list, team_member_delete

#Ten plik definiuje wzorce URL dla aplikacji 'team'.
#Mapuje ścieżki URL na odpowiednie widoki zdefiniowane w views.py.

urlpatterns = [
    path('', api_root, name='api_root'),  # Główny endpoint API, zwracający dostępne zasoby
    path('members/', team_member_list, name='team_member_list'), # Endpoint dla listy członków zespołu i dodawania nowych
    path('members/<int:pk>/', team_member_delete, name='team_member_delete'), # Endpoint do usuwania konkretnego członka zespołu
]
