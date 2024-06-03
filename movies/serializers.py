from rest_framework import serializers
from .models import *
from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

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
    
def overview_validator(value):
    if value > 300:
        raise ValidationError('소개 문구는 최대 300자 이하로 작성해야 합니다.')
    elif value < 10:
        return ValidationError('소개 문구는 최소 10자 이상으로 작성해야 합니다.')
    return value
    

# ModelSerializer 로 구현하기 (Django의 ModelForm 과 유사)
class MovieSerializer(serializers.ModelSerializer):
    # 이렇게 해도 상관 없음
    # name = serializers.CharField(read_only = True)
    # overview = serializers.CharField(write_only = True)
    
    # 길이 제한 유효성 검사
    # overview = serializers.CharField(validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=300)])
    
    # 유효성 검사 함수 만들어서 사용
    # overview = serializers.CharField(validator=[overview_validator])
    
    # 유일성 여부 확인
    # name = serializers.CharField(validators=[UniqueValidator(
    #     queryset=Movie.objects.all(), # 필수 옵션
    #     message='이미 존재하는 영화 이름입니다.'
    # )])
    
    # validate_[필드명] () 힘수
    # def validate_overview(self, value):
    #     if 10 <= len(value) and len(value) <= 300:
    #         return value
    #     raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')
    
    # validate() 함수
    def validate(self, attrs):
        if 10 > len(attrs['overview']) or len(attrs['overview']) > 300:
            raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')
        if len(attrs['name']) > 50:
            raise ValidationError('영화 이름은 50자 이하로 작성해주세요.')
        return attrs
    
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
        
        validators = [
            UniqueTogetherValidator(
                queryset=Movie.objects.all(),
                fields=['name', 'overview'],
            )
        ]
        
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