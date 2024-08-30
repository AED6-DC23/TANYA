from django_filters import FilterSet
from .models import *


class CommFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'post'
        }
        labels = {'post': 'Выбери пост'}

    def __init__(self, *args, **kwargs):
        super(CommFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(author__id=kwargs['request'])
