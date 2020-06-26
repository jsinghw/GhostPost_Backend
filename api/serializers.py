from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from django.utils import dateformat

from api.models import Post


# help understading vote_score
# https://django.cowhite.com/blog/dynamic-fields-in-django-rest-framwork-serializers/
class PostSerializer(ModelSerializer):
    vote_score = SerializerMethodField(method_name='calculate_vote_score')
    uploaded_date = SerializerMethodField(method_name='calculate_date_time')

    class Meta:
        model = Post
        fields = (
            'id',
            'boast_or_roast',
            'content',
            'upvotes',
            'downvotes',
            'vote_score',
            'uploaded_date'
        )

    def calculate_vote_score(self, instance):
        return (instance.upvotes - instance.downvotes)

    def calculate_date_time(self, instance):
        return (dateformat.format(instance.upload_date, 'g:i A M d,Y'))
        # return instance.upload_date


class UpvoteSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'upvotes',
        )


class DownvoteSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'downvotes',
        )
