from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):

    blogtitle = serializers.CharField(max_length=100)
    blogauthor = serializers.CharField(max_length=100)
    blogcontent = serializers.CharField(max_length=500)
    publishdate = serializers.DateField()
    blogcategory = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.blogtitle = validated_data.get('blogtitle', instance.blogtitle)
        instance.blogauthor = validated_data.get('blogauthor', instance.blogauthor)
        instance.blogcategory = validated_data.get('blogcategory', instance.blogcategory)
        instance.publishdate = validated_data.get('publishdate', instance.publishdate)
        instance.blogcontent = validated_data.get('blogcontent', instance.blogcontent)
        instance.save()
        return instance