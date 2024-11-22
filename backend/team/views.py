from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TeamMember
from .serializers import TeamMemberSerializer
from django.urls import reverse

#idok obsługujący żądania GET i POST dla listy członków zespołu.
@api_view(['GET', 'POST'])
def team_member_list(request):
    if request.method == 'GET':
        # Pobiera wszystkich członków zespołu z bazy danych
        members = TeamMember.objects.all()
        # Serializuje dane wielu obiektów TeamMember
        serializer = TeamMemberSerializer(members, many=True)
        # Zwraca zserializowane dane w odpowiedzi HTTP
        return Response(serializer.data)

    elif request.method == 'POST':
        # Tworzy serializer z danymi z żądania
        serializer = TeamMemberSerializer(data=request.data)
        # Sprawdza, czy dane są poprawne
        if serializer.is_valid():
            # Zapisuje nowy obiekt TeamMember w bazie danych
            serializer.save()
            # Zwraca zserializowane dane nowego obiektu z kodem statusu 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         # Jeśli dane są niepoprawne, zwraca błędy z kodem statusu 400 Bad Request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Widok obsługujący żądanie DELETE dla pojedynczego członka zespołu.
@api_view(['DELETE'])
def team_member_delete(request, pk):
    try:
        # Próbuje pobrać obiekt TeamMember o podanym pk
        member = TeamMember.objects.get(pk=pk)
    except TeamMember.DoesNotExist:
        # Jeśli obiekt nie istnieje, zwraca odpowiedź 404 Not Found
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Usuwa obiekt z bazy danych
    member.delete()
    # Zwraca odpowiedź 204 No Content po pomyślnym usunięciu
    return Response(status=status.HTTP_204_NO_CONTENT)

#Główny widok API, zwracający dostępne endpointy.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'members': request.build_absolute_uri(reverse('team_member_list')),
    })
