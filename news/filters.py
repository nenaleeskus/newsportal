from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Category
import django_filters
from django import forms


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Любая',
    )
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}),
                                     label="Опубликовано после: ", lookup_expr='date__gt')

    class Meta:
        model = Post
        fields = {

            'title': ['icontains'],
        }
