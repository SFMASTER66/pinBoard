# pinBoard

### App Deployment Instructions

*Requirements:*  
  Python 3, pip3, virtualenv

*First time install:*

1. Download the lastest packages from https://github.com/freon-lunarion/pinBoard/archive/master.zip
2. Unzip master.zip
3. Open terminal, go to unzipped directory
4. Make virtual enviroment by running: virtualenv venv 
5. Activate virtual environment : source venv/bin/active
6. Install dependencies with: pip install -r requirement.txt
7. Run: chmod +x setup.sh
8. Run: ./setup.sh
9. Follow the instructions to make super user (admin)


*Running the server:*

1. Activate the virtualenv with : source venv/bin/activate
2. Open terminal, go to master directory
3. Run: python manage.py runserver
4. Navigate to running server page (http://127.0.0.1:8000 port may be different based on system configuration)

### Feature Tryout Instructions

*Create Posts:*

1. Click the 'Create Post' button on the navigation bar.
2. Choose a type of post to create.
3. For images and youtube videos, input title and url to the resource.
4. For articles and questions, input title and detail of the post. Tags should be separated by comma.
5. Submit the post.


*Vote for Posts, Commments and Answers:*

1. Posts can be voted on home page, with self-sorting feature.
2. Click 'Open' button of a post, go to the post detail page.
3. Posts, Commments and Answers can be voted on post detail page.
4. Comments and Answers will be sorted by score after refreshing the page.


*Save Posts:*

1. Posts can be saved as favorite posts via the save button (heart shaped) on either home page or post detail page.
2. Favorited posts are displayed on user profile page.


*Pin Posts:*

1. Moderators (superusers) can pin posts on home page via the pin button on the card of the post.
2. Pinned posts are displayed on the top of home page.


*Search Posts:*

1. Input in the search bar on the navigation bar, type enter to start the search.
2. Add 'post', 'image', 'youtube' or 'question' to the keywords for searching articles only, images only, videos only or questions only.
3. Type '#' at the beginning to search tags. Tags should be separated by a comma.


*Quiz Sets & Quizzes:*

1. Go to the quiz sets page by clicking the Quiz Sets button in the nav bar.
2. Create a new Quiz Set via the Create Set button
3. Give the set a title and description, as well as the minimum score for a successful quiz tryout (attempt) and number of questions to display during tryout.
4. Click Submit button to create the set.
5. Open an existing quiz set by clicking Open at the bottom of its card.
6. Add new questions via the '...' button followed by the blue New Question button.
7. Type in the question in the detail box, and provide up to 4 multiple choice options in the options areas, being sure to choose which of the options is the right answer.
8. Click the Submit button to add the question to the quiz set.
9. Tryout a quiz via the '...' button followed by the red Tryout button.
10. Clicking the blue tick button on completion gives your results.


*Leaderboard:*

1. Click the 'Leaderboard' button on the navigation bar.
2. Top ten users with highest scores are displayed.


*User Profile:*

1. Click the 'Hello, Username' button on the navigation bar.
2. The user's favorite posts, top five posts with highest scores, all types of posts and quiz sets are displayed on the user profile page.
3. User avatar can be uploaded by clicking the avatar image.

### How To View Source Code

*File Structure:*

pinBoard
 - blogs (folder)
 - quiz (folder)
 - shared (folder)
 - livesession (folder)
 - pinBoard (folder)
 - sample (folder)
 - ... (files)
 
1. Open the root pinBoard folder with PyCharm.
2. There are three apps in this project: blogs, quiz and shared. The blogs app is for features dealing with posts, the quiz app is for quiz set feature, and the shared app is for handling shared models and pages such as the user profile model and the user profile page.
3. Backend codes, including the methods to render pages and the api methods, are in blogs/views.py, quiz/views.py and shared/views.py.
4. Frontend codes are under blogs/templates/, quiz/templates/ and shared/templates/.
5. Note that data model is setup for livesession app, but this app is not implemented due to time limit. So it is not installed, and only for further development.

### REST APIs (Most are login required except for log in, log out and register)

*blogs app (blogs/view.py):*

| endpoint      | method           | description  | arguments  |
| ------------- | ------------- | ----- | ----- |
| /blogs/      | GET | Render home page | - |
| /blogs/      | GET      |   Search by tags |   tags(url) |
| /blogs/ | GET      |    Search by title |    title(url) |
| /blogs/<post_id>/ | GET      |    Render post detail page |    - |
| /blogs/<post_id>/ | POST      |    Create comment or question answer |  detail(body)   |
| /blogs/<post_id>/ | PUT      |   Set question answer correct |  action(body)   |
| /blogs/createArticlePost/ | POST      |    Create article post |    title(body), detail(body), tags(body, optional) |
| /blogs/createImagePost/ | POST      |    Create image post |    title(body), detail(body) |
| /blogs/createYoutubePost/ | POST      |    Create video post |    title(body), detail(body) |
| /blogs/createQuestion/ | POST      |    Create Qna Question |    title(body), detail(body), tags(body, optional) |
| /blogs/<post_id>/pin/ | PUT      |    Pin a post or a question |    - |
| /blogs/<post_id>/unpin/ | PUT      |    Unpin a post or a question |    - |
| /blogs/login/ | GET      |    Render log in page |  - |
| /blogs/login/ | POST      |    Log in |   username(body), password(body) |
| /blogs/logout/ | GET      |    Log out |  - |
| /blogs/register/ | GET      |    Render log out page |   - |
| /blogs/register/ | POST      |    User register |  username(body), email(body), name(body), password(body), repassword(body) |
| /blogs/reset/ | PUT      |    Reset password |    newpassword(body), renewpassword(body) |

*shared app (shared/view.py):*

| endpoint      | method           | description  | arguments  |
| ------------- | ------------- | ----- | ----- |
| /vote/      | GET | Get the existence of voting for certain content from certain user | - |
| /vote/      | PUT      |   Add value of 'vote' argument to the content score (insert a record to Vote model) |   vote(body) |
| /user_avatar/ | PUT      |    Modify user avatar |    avatar(body) |
| /user/<user_id> | GET      |    Render user profile page |    - |
| /<post_id>/like/ | PUT      |    Add a post to a user's favorite list |  -   |
| /<post_id>/unlike/ | PUT      |    Remove a post from a user's favorite list |  -   |
| /user/ | GET      |  Get top ten user data for leaderboard |  -   |


# Reference Documents
*Python3 & pip*

* Mac: https://docs.python-guide.org/starting/install3/osx/
* Linux https://docs.python-guide.org/starting/install3/linux/
* Windows: https://docs.python-guide.org/starting/install3/win/

*Virtualenv*

* Mac: https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv
* Linux: https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv
* Windows: https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv

Django 2.1 : https://docs.djangoproject.com/en/2.1/
