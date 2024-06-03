from rest_framework import serializers
from .models import *

# 사용할 필드 이름은 꼭 모델에서 사용하는 필드 이름과 일치!! 

# class MovieSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # opening_date = serializers.DateField()
    # running_time = serializers.IntegerField()
    # overview = serializers.CharField()
    
    # # validated_data는 유효성 검사를 마친 데이터 의미
    # # MovieSerializer 필드들에 해당하는 데이터가 딕셔너리 형태로 전달
    # def create(self, validated_data):
    #     # 언패킹(**) : 리스트나 딕셔너리 형태로 감싸져 있는 값을 풀어서 사용하는 것
    #     return Movie.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     # get() 함수로 validated_data에 값이 존재한다면 수정 요청한 값을, 없다면 instance.name을 넣고 데이터 수정
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.opening_date = validated_data.get('opening_date', instance.opening_date)
    #     instance.running_time = validated_data.get('running_time', instance.running_time)
    #     instance.overview = validated_data.get('overview', instance.overview)
    #     instance.save()
        
    #     return instance
    
# ModelSerializer 로 구현하기 (Django의 ModelForm 과 유사)
class MovieSerializer(serializers.ModelSerializer):
    # 이렇게 해도 상관 없음
    # name = serializers.CharField(read_only = True)
    # overview = serializers.CharField(write_only = True)
    
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
        
        # fields = '__all__' # 모델에 존재하는 모든 필드 사용
        # exclude = ['overview'] # exclude 안에 있는 필드를 제외하고 사용
        # read_only_fields = ['name'] # id를 제외한 필드에 선택적으로 read_only를 추가하기 위해 read_only_fields 사용
        
        # 다양한 필드에 여러 옵션을 추가할 경우 extra_kwargs 사용
        # extra_kwargs = {
            # 'overview' : {'write_only' : True},
        # }
        
# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     gender = serializers.CharField()
#     birth_date = serializers.DateField()
    
#     def create(self, validated_data):
#         return Actor.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.birth_date = validated_data.get('birth_date', instance.birth_date)
    
class ActorSerializer(serializers.ModelSerializer):
    model = Actor
    fields = ['id', 'name', 'gender', 'birth_date']