from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import F

from api.serializers import PostSerializer, UpvoteSerializer
from api.models import Post


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None, format=None):
        sp_post = self.get_object()
        sp_post['upvotes'] = request.data['upvotes']
        sp_post.save()

    @action(detail=False)
    def boasts(self, request):
        boast_posts = Post.objects.filter(
            boast_or_roast='B').order_by('-upload_date')

        page = self.paginate_queryset(boast_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(boast_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roast_posts = Post.objects.filter(
            boast_or_roast='R').order_by('-upload_date')

        page = self.paginate_queryset(roast_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(roast_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_vote_scores(self, request):
        vote_scores = Post.objects.all().order_by(
            -(F('upvotes') - F('downvotes'))
        )

        page = self.paginate_queryset(vote_scores)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(vote_scores, many=True)
        return Response(serializer.data)
