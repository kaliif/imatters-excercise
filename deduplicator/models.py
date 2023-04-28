from django.db import models


class SequenceModel(models.Model):
    sequence = models.TextField(primary_key=True)

    @classmethod
    def test_sequence(cls, sequence: str) -> bool:
        try:
            cls.objects.get(pk=sequence)
            return True
        except cls.DoesNotExist:
            cls(pk=sequence).save()
            return False

    @classmethod
    def clear_sequences(cls) -> None:
        cls.objects.all().delete()
