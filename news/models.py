from django.contrib.auth.models import User
from django.db import models
from .res import *
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(author=self).aggregate(models.Sum('rating'))
        author_comment_rating = Comment.objects.filter(user=self.user).aggregate(models.Sum('rating'))
        all_comment_rating = Comment.objects.filter(post__in=Post.objects.filter(author=self)).aggregate(
            models.Sum('rating'))
        self.rating = post_rating['rating__sum'] * 3 + \
                      author_comment_rating['rating__sum'] + \
                      all_comment_rating['rating__sum']


class Category(models.Model):
    name = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=sport, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_choice = models.CharField(max_length=2, choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=244)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return self.text[:124] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.id}, {self.author.user.username}, {self.type_choice}, {self.date}, ' \
               f'{self.title}, {self.text[:20]}, {self.rating}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=244)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
