from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Movie, Actor, Review
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer

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

# GET (특정한 영화 데이터 조회), PATCH (특정한 영화 데이터 수정), DELETE (특정한 영화 데이터 삭제)
@api_view(['GET', 'PATCH', 'DELETE'])
def movie_detail(request, pk):
    
    movie = get_object_or_404(Movie, pk=pk) # 함수의 첫 번째 파라미터로는 조회할 모델, 두 번째 파라미터로는 조회할 pk값
    # 존재하지 않는 데이터를 요청하면 get_object_or_404() 함수는 이런 상황에 자동으로 404 에러 발생시킴
    if request.method == 'GET':
        serializer = MovieSerializer(movie) # 오직 1개의 데이터를 조회하기 때문에 many옵션 필요 없음
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        # 부분 데이터 수정이기 때문에 partial=True, 
        # 모든 데이터를 수정하는 PUT 요청이면 partial 옵션 사용x
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        movie.delete()
        # 데이터가 삭제되면 반환할 데이터가 없기 때문에 204 반환
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    

@api_view(['GET', 'PATCH', 'DELETE'])
def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    
    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def review_list(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'GET':
        # movie=movie 를 전달하여 영화 ID 기준으로 작성된 리뷰 데이터를 가지고 올 수 있음
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        
        if serializer.is_valid():
            # ReviewSerializer 에서 영화 데이터를 직접 입력 받지 않고 URL에서 pk 값을 기준으로
            # 입력 받기 때문에 save()에 movie 를 전달한 것
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    




