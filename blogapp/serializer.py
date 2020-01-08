from rest_framework import serializers

from blogapp.models import PostType, Post


class PostTypeSerializer(serializers.ModelSerializer):  # model staff
    class Meta:
        model = PostType
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):  # model staff
    class Meta:
        model = Post
        fields = "__all__"
