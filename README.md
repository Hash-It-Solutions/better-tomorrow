<h2>Introduction</h2>
<h3>Purpose: </h3>
The purpose of this document is to specify the requirements for an e-learning website built with Django.
<h3>Scope:</h3>
The scope of this website includes the following features:
<ul>
    <p><b>Courses:</b> The website will allow users to browse and purchase courses. Each course will have a description and a list of subjects.</p> 
    <p><b>Modules:</b> Each course will be divided into modules, which will contain notes, mock tests, and class recordings.</p> 
    <p><b>Notes:</b> Users will be able to view and download notes for each module.</p> 
    <p><b>Mock Tests: </b> Users will be able to take mock tests for each module. Each mock test will consist of a series of questions with multiple choice options.</p> 
    <p><b>Class Recordings:</b> Users will be able to view class recordings for each module.</p> 
    <p><b>Subscriptions:</b> Users will be able to purchase subscriptions to access all courses and modules.</p> 
</ul>
<h3>Definitions, acronyms, and abbreviations:</h3>
<ul>
    <li><b>E-learning:</b> Electronic learning, or learning through electronic media.</li>
    <li><b>Django:</b> A web framework written in Python.</li>
    <li><b>SRS:</b> Software Requirements Specification.</li>
</ul>
<h2>Overall Description</h2>
<h3>Product perspective:</h3>
The e-learning website will be a web-based application built with Django. It will allow users to browse and purchase courses, view and download notes, take mock tests, view class recordings, and purchase subscriptions to access all courses and modules.
<h3>Product functions:</h3>
The e-learning website will have the following functions:
<ul>
    <li><b>Course browsing:</b> Users will be able to browse a list of available courses and view details for each course, including the course description and list of subjects.</li>
    <li><b>Course purchasing:</b> Users will be able to purchase courses using a payment gateway such as Stripe or PayPal.</li>
    <li><b>Module viewing:</b> Users who have purchased a course will be able to view the modules for that course. Each module will contain notes, mock tests, and class recordings.</li>
    <li><b>Note viewing and downloading:</b> Users who have purchased a course will be able to view and download notes for each module.</li>
    <li><b>Mock test taking:</b> Users who have purchased a course will be able to take mock tests for each module. Each mock test will consist of a series of questions with multiple choice options. Users will be able to view their score after completing the test.</li>
    <li><b>Class recording viewing:</b> Users who have purchased a course will be able to view class recordings for each module.</li>
    <li><b>Subscription purchasing:</b> Users will be able to purchase subscriptions to access all courses and modules.</li>
</ul>
<h3>User characteristics:</h3>
The e-learning website will be used by individuals who are interested in learning new subjects through online courses.
<h3>Constraints:</h3>
The e-learning website will be built using Django, and will require a web server and database server to host the application.
<h2>External Interface Requirements</h2>
<h3>User interface:</h3>
The e-learning website will have a user-friendly interface with the following features:
<ul>
    <li><b>Course listings:</b> The homepage will display a list of available courses, with the option to view more details for each course.</li>
    <li><b>Course details:</b> The course details page will display the course description, list of subjects, and a list of modules.</li>
    <li><b>Module details:</b> The module details page will display the module title, description, and a list of notes, mock tests, and class recordings.</li>
    <li><b>Note viewing:</b> The note viewing page will display the note title and content.</li>
    <li><b>Mock test taking:</b> The mock test taking page will display a series of questions with multiple choice options.</li>
    <li><b>Class recording viewing:</b> The class recording viewing page will display the class recording title and a video player.</li>
    <li><b>Subscription details:</b> The subscription details page will display the subscription title, description, and price.</li>
</ul>
<h3>Hardware interface:</h3>
The e-learning website will be hosted on a web server and database server.
<h3>Software interface:</h3>
The e-learning website will be built with Django, and will require a web server and database server to host the application.
<h2>Functional Requirements</h2>
<h3>Course browsing:</h3>
The e-learning website will allow users to browse a list of available courses and view details for each course, including the course description and list of subjects.
<h3>Course purchasing:</h3>
The e-learning website will allow users to purchase courses using a payment gateway such as Stripe or PayPal.
<h3>Module viewing:</h3>
Users who have purchased a course will be able to view the modules for that course. Each module will contain notes, mock tests, and class recordings.
<h3>Note viewing and downloading:</h3>
Users who have purchased a course will be able to view and download notes for each module.
<h3>Mock test taking:</h3>
Users who have purchased a course will be able to take mock tests for each module. Each mock test will consist of a series of questions with multiple choice options. Users will be able to view their score after completing the test.
<h3>Class recording viewing:</h3>
Users who have purchased a course will be able to view class recordings for each module.
<h3>Subscription purchasing:</h3>
Users will be able to purchase subscriptions to access all courses and modules.
<h2>Non-Functional Requirements</h2>
<h3>Performance requirements:</h3>
The e-learning website will be able to handle a large number of users at the same time.
<h3>Security requirements:</h3>
The e-learning website will use HTTPS to encrypt all data sent between the user and the server.
<h3>Software quality attributes:</h3>
The e-learning website will be easy to use and maintain.
<h3>Business rules:</h3>
The e-learning website will allow users to purchase courses using a payment gateway such as Stripe or PayPal.
<h2>Other Requirements</h2>
<h3>Legal requirements:</h3>
The e-learning website will comply with all applicable laws and regulations.
<h3>Regulatory requirements:</h3>
The e-learning website will comply with all applicable laws and regulations.
<h3>USER APIs</h3>
<h3>Insert User</h3>
<ul>
    <p>Insert a course into the database</p>
    <p>URL: /api/CourseApi/CourseApi/</p>
    <p>Method: GET, POST, HEAD, OPTIONS</p>
    <p>URL Content-Type: application/json</p>
    
       
        Example Input body:
        {
        "id": 1,
        "name": "test",
        "description": "description"
        }
      
</ul>