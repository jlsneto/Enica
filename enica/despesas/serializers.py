from rest_framework import serializers
from .models import Despesa,Categoria,Parcela

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = '__all__'
        read_only_fields=['pk','despesa','numero_parcela'] # Já adiciona sozinho.

class DespesaSerializer(serializers.ModelSerializer):
    parcelas = ParcelaSerializer(many=True)
    class Meta:
        model = Despesa
        fields = '__all__'
        read_only_fields = ['pk','quantidade_parcela']

    # Foi necessário sobrescrever devido as parcelas.
    def create(self,validated_data):
        parcelas = validated_data.pop('parcelas')
        validated_data['quantidade_parcela'] = len(parcelas)
        despesa = Despesa.objects.create(**validated_data)
        parcela_num = 1
        for parcela in parcelas:
            parcela['numero_parcela'] = parcela_num
            parcela_num += 1
            Parcela.objects.create(despesa=despesa, **parcela)
            print("Adicionado despesa!")
        return despesa


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

