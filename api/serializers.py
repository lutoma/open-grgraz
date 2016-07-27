from rest_framework import serializers
from api.models import *


class ParliamentaryGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParliamentaryGroup
        fields = ('id', 'name')


class ParliamentarySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParliamentarySession
        fields = ('session_date',)


class CouncilPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilPerson
        fields = ('name', 'academic_degree', 'email', 'parliamentary_group')


class MotionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionType
        fields = ('name',)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('long_filename', 'short_filename', 'path')


class MotionSerializer(serializers.ModelSerializer):
    session = serializers.StringRelatedField()
    motion_type = serializers.StringRelatedField()
    proposer = CouncilPersonSerializer()
    files = FileSerializer(many=True)

    class Meta:
        model = Motion
        fields = ('id', 'session', 'title', 'motion_type', 'parliamentary_group',
                  'proposer', 'files', 'answer')
