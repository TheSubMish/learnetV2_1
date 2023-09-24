from .models import Course,Chapter,Test

def create_test(form_data,slug):
    course = Course.objects.get(slug=slug)
    Test.objects.create(
        course = course,
        title = form_data.get('title'),
        question = form_data.get('question'),
        option1 = form_data.get('option1'),
        option2 = form_data.get('option2'),
        option3 = form_data.get('option3'),
        option4 = form_data.get('option4'),
        corAns = form_data.get('corAns')
    )