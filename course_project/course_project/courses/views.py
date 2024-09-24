from django.shortcuts import render, redirect
import json
import os


COURSE_LIST_JSON_PATH = os.path.join(os.path.dirname(__file__), 'get_all_courses_API_response.json')
COURSE_DETAIL_JSON_PATH = os.path.join(os.path.dirname(__file__), 'get_course_detail_API_response.json')


def course_list(request):

    with open(COURSE_LIST_JSON_PATH, 'r') as json_file:
        data = json.load(json_file)


    courses = data.get('courses', [])
    filters = data.get('facets', {})


    applied_filters = request.GET.getlist('filter', [])
    if applied_filters:
    
        filtered_courses = [course for course in courses if any(f in course['category'] for f in applied_filters)]
    else:
        filtered_courses = courses
    print(filtered_courses)
    return render(request, 'course_list.html', {
        'courses': filtered_courses,
        'filters': filters,
        'applied_filters': applied_filters
    })



# Course Detail View
def course_detail(request, course_id):

    with open(COURSE_DETAIL_JSON_PATH, 'r') as f:
        data = json.load(f)

    
    videos = data.get("videos") if str(course_id) == data.get("course_id") else []

    if videos:  
        print(videos[0].get("youtube_url"))
    else:
        print("No videos found for this course.")

    context = {
        'videos': videos,
    }

    return render(request, 'course_detail.html', context)
        
        