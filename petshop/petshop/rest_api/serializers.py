from rest_framework.serializers import ModelSerializer

from reserva.models import reserva

class agendamentomodelserializers(ModelSerializer):
    class Meta:
        model = reserva
        fields ='__all__'