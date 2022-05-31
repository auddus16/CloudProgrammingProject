import os.path

from django.contrib.auth.models import User
from django.db import models
from markdown import markdown
from markdownx.models import MarkdownxField

# Category
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # URL에 들어갈 수 있는 문자열 필드

    # method
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/menu/category/{self.slug}/'

    # 복수형 내가 정하고 싶을 때 (inner class)
    class Meta:
        verbose_name_plural = 'Categories'


# Menu
class Menu(models.Model):

    name = models.CharField(max_length=30)
    price = models.IntegerField
    content = MarkdownxField(max_length=50)
    image = models.ImageField(upload_to='menu/images/%Y/%m/%d/', blank=True)   # 이미지가 없어도 괜찮다. blank 속성 값 지정
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # methods
    def __str__(self):
        return f'[{self.pk}]  [{self.name}] :: {self.price}'

    def get_absolute_url(self):
        return f'/menu/{self.name}/'

    # def get_file_name(self):    # 파일명이 경로가 아닌 이름으로 나오게 끔, 백에서
    #     return os.path.basename(self.attached_file.name)

    def get_markdown_content(self):
        return markdown(self.content)

class Order(models.Model):
    price = models.IntegerField
    waitnum = models.IntegerField
    store = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.waitnum} - {self.store} - {self.price}'

    # def get_absolute_url(self):
    #     return f'{self.post.get_absolute_url()}#comment-{self.pk}'