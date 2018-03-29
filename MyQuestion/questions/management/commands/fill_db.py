from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Answer, Tag
import random
from datetime import datetime    
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 20):
            u = User.objects.get(id=1)
            t = Tag.objects.get(word='test_tag')
            titlename= 'Test Question ' + str(i)
            exampletext = 'Examples of closed-ended questions are: Are you feeling better today? May I use the bathroom? Is the prime rib a special tonight?'
            q = Question(author = u, title = titlename, text = exampletext, rating = random.randint(-10, 10), date = datetime.now())
            q.save()
            q.tags.add(t)
            exampleanswer = 'Closed-ended questions should not always be thought of as simple questions that anyone can quickly answer merely because they require a yes or no answer. '
            a = Answer(question_id=q.id, author = u, text = exampleanswer, rating = random.randint(-10, 10), date = datetime.now(), correct=False)
            a.save()
            self.stdout.write(self.style.SUCCESS('Successfully added item "%s"' % i))