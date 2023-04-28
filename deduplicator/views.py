from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import SequenceModel


@api_view(["POST"])
def test_sequence(request, sequence):
    if request.method == "POST":
        result = SequenceModel.test_sequence(sequence)
        return JsonResponse(
            {"duplicate": result},
            status=status.HTTP_200_OK,
        )


@api_view(["PUT"])
def clear_sequences(request):
    if request.method == "PUT":
        SequenceModel.clear_sequences()
        return JsonResponse({}, status=status.HTTP_200_OK)
