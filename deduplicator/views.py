from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import SequenceModel


# curl -w ", %{http_code}\n" -X POST  http://localhost:8080/sequence/sdfsdf
@api_view(["POST"])
def test_sequence(request, sequence):
    if request.method == "POST":
        result = SequenceModel.test_sequence(sequence)
        return JsonResponse(
            {"duplicate": f"{result}"},
            status=status.HTTP_200_OK,
        )


# curl -o /dev/null -s -w "%{http_code}\n" -X PUT http://localhost:8080/clear
@api_view(["PUT"])
def clear_sequences(request):
    if request.method == "PUT":
        SequenceModel.clear_sequences()
        return JsonResponse({}, status=status.HTTP_200_OK)
