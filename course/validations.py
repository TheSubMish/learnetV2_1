from .models import Course

def course_validate(error_msg_dict):
    error = {
        'courseTitle': '',
        'courseDescrip': '',
        'category': '',
        'courseImage': ''
    }

    try:
        if error_msg_dict['category']:
            error['category'] = "Select Category Of Your Course"
            return error
    except KeyError:
        pass

    error_msg = error_msg_dict['__all__'][0]['message']
    
    if 'Name' in error_msg:
        error['courseTitle'] = error_msg
    if 'Description' in error_msg:
        error['courseDescrip'] = error_msg
    if 'category' in error_msg:
        error['category'] = error_msg
    if 'Image' in error_msg:
        error['courseImage'] = error_msg
    return error

def chapter_validate(error_msg_dict):
    error = {
        'course': '',
        'chapterName': '',
        'chapterBody': ''
    }
    error_msg = error_msg_dict['__all__'][0]['message']
    if 'Course' in error_msg:
        error['course'] = error_msg
    if 'Name' in error_msg:
        error['chapterName'] = error_msg
    if 'Content' in error_msg:
        error['chapterBody'] = error_msg
    return error

def test_validate(form_data):
    error = {
        'course': '',
        'title': '',
        'question': '',
        'option1': '',
        'option2': '',
        'option3': '',
        'option4': '',
        'corAns': ''
    }

    if form_data.get('course') == '':
        error['course'] = 'Course Name Cannot Be Empty'
    elif form_data.get('title') == '':
        error['title'] = 'Test Title Cannot Be Empty'
    elif form_data.get('question') == '':
        error['question'] = 'Question Field Cannot Be Empty'
    elif form_data.get('option1') == '':
        error['option1'] = 'Option One Field Cannot Be Empty'
    elif form_data.get('option2') == '':
        error['option2'] = 'Option Two Field Cannot Be Empty'
    elif form_data.get('option3') == '':
        error['option3'] = 'Option Three Field Cannot Be Empty'
    elif form_data.get('option4') == '':
        error['option4'] = 'Option Four Field Cannot Be Empty'
    elif form_data.get('corAns') == '':
        error['corAns'] = 'Correct Answer Field Cannot Be Empty'
    else:
        return None
    
    return error