from records_app.models import Record
from django_filters import rest_framework as filters


class RecordFilter(filters.FilterSet):
    class Meta:
        model = Record
        fields = '__all__'
