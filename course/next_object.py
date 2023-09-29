from .models import Chapter

def get_next_chapter(course, current_chapter_id):
    chapters = Chapter.objects.filter(course=course).order_by('id')
    
    current_chapter_index = next((
        index for index, 
        chapter in enumerate(chapters) 
        if chapter.id == current_chapter_id
    ), None)
    
    if current_chapter_index is not None and current_chapter_index + 1 < len(chapters):
        return chapters[current_chapter_index + 1]
    
    return None