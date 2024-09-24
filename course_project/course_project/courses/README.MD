Course List and Detail Pages - Django Project
Overview
This project implements a simple course listing and detail interface using Django. The system consists of two main pages:

Page 1: Course List

Displays a list of available courses.
Provides filters based on the facets section of the get_all_courses_API_response.json file.
Clicking on a course will redirect the user to the course detail page.
Page 2: Course Detail

Shows detailed information for the selected course.
Lists all the videos associated with the course, using the get_course_detail_API_response.json file.
Allows users to play videos upon selection, following a predefined design layout.
File Structure
Copy code
├── course_list/
│   ├── templates/
│   │   ├── course_list.html  # Page 1 template
│   │   ├── course_detail.html  # Page 2 template
│   └── views.py  # Handles course listing and detail views
│
│
├── get_all_courses_API_response.json  # JSON file containing all courses
├── get_course_detail_API_response.json  # JSON file containing course details
├── urls.py  # URL routing
└── README.md  # Project documentation
Setup
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd course_list_project
Install Dependencies: Ensure you have Django installed. If not, you can install it using pip:

bash
Copy code
pip install django
Run the Project:

bash
Copy code
python manage.py runserver
Access the App: Open your browser and go to http://localhost:8000/ to access the course list page.

Features
Page 1: Course List
The courses are listed based on the data in the get_all_courses_API_response.json file.
Filters are dynamically generated from the facets section in the JSON file.
Each course title is clickable, redirecting to the corresponding course detail page.
Page 2: Course Detail
Displays the details of the selected course, including all related videos.
Users can click on a video to play it within the page, as per the provided design_2 layout.
How to Use
Course List Page:

Browse available courses, and apply filters to refine your search.
Click on any course to see the course details.
Course Detail Page:

View the course description and list of videos.
Select any video to play it directly on the page.
JSON Files
get_all_courses_API_response.json: Contains the data for all courses, including facets for filtering.
get_course_detail_API_response.json: Contains detailed information for individual courses, including the list of videos.
Future Enhancements
Add user authentication for personalized experiences.
Implement pagination for the course list page.
Enhance video playback features (e.g., full-screen mode).
