from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from records_app.models import Record


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custome claim: username
        token['username'] = user.username
        return token


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'

    def to_internal_value(self, data):
        # new_data = data.copy()
        # new_data['base_station'] = self.context['request'].query_params.get(
        #     'base_station_id')
        # if new_data.get('error') is None:
        #     new_data['error'] = 'EMPTY'
        # internal_value = super(GrowingToolSerializer,
        #                        self).to_internal_value(new_data)
        # # Add growing_tool_type_id to validated_data
        # growing_tool_type_id = data.get('growing_tool_type_id')
        # if self.context['request'].method in ['POST']:
        #     if not growing_tool_type_id:
        #         raise serializers.ValidationError({
        #             'growing_tool_type_id': 'This field is required.'
        #         })
        #     internal_value.update({
        #         "growing_tool_type_id": growing_tool_type_id
        #     })

        return data
