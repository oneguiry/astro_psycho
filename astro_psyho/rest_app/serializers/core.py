from rest_framework import serializers

from core.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=40)
    body = serializers.CharField()


class NewsDetailSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=40)
    body = serializers.CharField()
    author = serializers.IntegerField()
    pub_date = serializers.DateField()
