from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True) # 여러 데이터를 직렬화 할 때 many=True
        # MovieSerializer에 파이썬 객체 형태의 데이인 movies를 넣어 주면 데이터가
        # 딕셔너리 형태로 바뀜 -> 변환된 데이터에는 serializer.data 로 접근 할 수 있음
        
        # Response 는 DRF에서 제공 -> 파이썬 딕셔너리로 변환된 데이터는 Response 에서 JSON 형태로 바뀜
        return Response(serializer.data, status=200)
    
    elif request.method == 'POST':
        # POST 요청으로 전달된 데이터는 request.data로 접근
        data = request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        data = request.data
        serializer = ActorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



