from rest_framework import serializers
from .models import *

# 사용할 필드 이름은 꼭 모델에서 사용하는 필드 이름과 일치!! 

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()
    
    # validated_data는 유효성 검사를 마친 데이터 의미
    # MovieSerializer 필드들에 해당하는 데이터가 딕셔너리 형태로 전달
    def create(self, validated_data):
        # 언패킹(**) : 리스트나 딕셔너리 형태로 감싸져 있는 값을 풀어서 사용하는 것
        return Movie.objects.create(**validated_data)


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()
    
    def create(self, validated_data):
        return Actor.objects.create(**validated_data)
    
