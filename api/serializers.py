from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import SerializerMethodField

from api.models import Post


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
            'id',
            'upvotes'
        )
