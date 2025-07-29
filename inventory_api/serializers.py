from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'status',
                  'creation_date', 'update_date']

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
        if 'status' in data:
            status_value = data['status']
            if isinstance(status_value, str):
                if status_value.lower() == 'activo' or status_value.lower() == 'true':
                    data['status'] = True
                elif status_value.lower() == 'inactivo' or status_value.lower() == 'false':
                    data['status'] = False
                else:
                    raise serializers.ValidationError({"status": "El estatus debe ser 'activo', 'inactivo', 'true' o 'false'."})
            elif not isinstance(status_value, bool):
                raise serializers.ValidationError({"status": "El estatus debe ser un booleano (true/false) o una cadena ('activo'/'inactivo')."})
        return super().to_internal_value(data)
