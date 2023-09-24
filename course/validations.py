def course_validate(form_data):
    error = {
        'courseTitle': '',
        'courseDescrip': '',
        'courseImage': ''
    }

    if form_data.get('courseTitle') == '':
        error['courseTitle'] = 'Course Title Cannot Be Empty'
    elif form_data.get('courseDescrip') == '':
        error['courseDescrip'] = 'Course Description Cannot Be Empty'
    elif form_data.get('courseImage') == '':
        error['courseImage'] = 'Image Field Cannot Be Empty'
    else:
        return None
    
    return error

def chapter_validate(form_data):
    error = {
        'course': '',
        'chapterName': '',
        'chapterBody': ''
    }

    if form_data.get('course') == '':
        error['course'] = 'Course Name Cannot Be Empty'
    elif form_data.get('chapterName') == '':
        error['chapterName'] = 'Chapter Name Cannot Be Empty'
    elif form_data.get('chapterBody') == '':
        error['chapterBody'] = 'Chapter Content Cannot Be Empty'
    else:
        return None
    
    return error

def test_vlaidate(form_data):
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