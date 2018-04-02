from django import template

from questions.models import Tag, Profile
from django.db.models import Count
register = template.Library()

@register.inclusion_tag('subtemplates/popular_tags.html')
def show_popular_tags():
	tags = Tag.objects.annotate(q_count=Count('question')) \
                                 .order_by('-q_count')[:10]
	return {'tags': tags}

@register.inclusion_tag('subtemplates/best_users.html')
def show_best_users():
	profiles = Profile.objects.order_by('-rating')[:5]
	return {'profiles': profiles}