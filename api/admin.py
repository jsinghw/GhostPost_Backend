from django.contrib import admin
from api.models import Post


admin.site.register(Post)

# @admin.site.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ("name", "vote_scores")
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         queryset = queryset.annotate(
#             _vote_scores=('upvotes'-'downvotes'),
#         )
#         return queryset
#
#     def vote_scores(self, obj):
#         return obj._vote_scores
