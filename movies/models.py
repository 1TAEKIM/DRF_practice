from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=30)
    opening_date = models.DateField()
    running_time = models.IntegerField()
    overview = models.TextField()
    actors = models.ManyToManyField('Actor', related_name='movies')

    # 이와 같이 정의하면 영화 객체를 출력할 때 이름이 나옴
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    # ForeignKey는 1(영화) : N(리뷰) 관계를 표현
    # 역관계 이름을 바꾸기 위해서 related_name 옵션 사용
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=30)
    star = models.IntegerField()
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    # __str__() 함수는 모델 객체를 문자열로 나타낼 때 사용
    def __str__(self):
        # 위와 같이 정의하고 리뷰 객체를 출력하면 리뷰의 comment 필드 출력
        # 이와 같이, DRF에서는 관계를 직렬화할 때 관련된 객체의 __str__() 메소드가 사용되도록 할 수 있다.
        # --> 이때 사용하는 필드가 StringRelatedField
        return self.comment

# 1번 영화의 리뷰들을 조회하는 방법 (역관계를 사용하는 경우)
# Movie와 Review의 관계는 1:N 관계이기 때문에, 특정한 Movie 객체를 참조하는 Review 정보들은
# review_set에 담겨있습니다. (역관계 이름은 [역관계를 가지는 모델명]_set 형태로 사용할 수 있습니다.)
# movie = Movie.objects.get(pk=1)
# reviews = movie.review_set.all()
