from rest_framework import serializers

from academics.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model=Course

        fields="__all__"

        read_only_fields=["id","last_updated_date","trainer_info"]