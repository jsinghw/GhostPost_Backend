from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from api.models import Post


# help understading vote_score
# https://django.cowhite.com/blog/dynamic-fields-in-django-rest-framwork-serializers/
class PostSerializer(ModelSerializer):
    vote_score = SerializerMethodField(method_name='calculate_vote_score')

    class Meta:
        model = Post
        fields = (
            'id',
            'boast_or_roast',
            'content',
            'upvotes',
            'downvotes',
            'vote_score',
            'upload_date'
        )

    def calculate_vote_score(self, instance):
        return (instance.upvotes - instance.downvotes)


class UpvoteSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'upvotes',
        )
