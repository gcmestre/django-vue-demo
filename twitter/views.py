from .models import Tweet
from rest_framework import viewsets
from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users create of view a specific tweet or a list of tweets.
    """
    queryset = Tweet.objects.all().order_by('-created_date', 'name')
    serializer_class = TweetSerializer
