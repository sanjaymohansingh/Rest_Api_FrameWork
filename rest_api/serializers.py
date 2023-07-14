from rest_framework import serializers
from .models import Post


# Manual Serializer ------------------------------------------------------------------------
# class PostSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(default='')
#     price = serializers.IntegerField()

#     def create(self, validate_data):
#         return Post.objects.create(validate_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', validated_data.title)
#         instance.author = validated_data.get('author', validated_data.author)
#         instance.email = validated_data.get('email', validated_data.email)
#         instance.price = validated_data.get('price', validated_data.price)
# -------------------------END-------------------------------

# Using Model Serializer ------------------------------------
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'author', 'email', 'price']