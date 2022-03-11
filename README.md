# Author

Jerusha Otieno

# Description

This is a flask application allowing users to post one minute pitches. Other users can then vote on them and leave comments togive their feedback on them. Pitches are organized by category with new posts displayed first. 

# Live Link

View Site: https://pitches1-app.herokuapp.com/

# User Story

A user can:
* See the pitches other people have posted.
* Vote on the pitch they liked and give it a downvote or upvote.
* Sign in to leave a comment
* Receive a welcoming email once I sign up.
* View pitches created in their profile page.
* Comment on the different pitches and leave feedback.
* Submit a pitch in any category.
* View the different categories.

# BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | On page load | Get all posts; Select between signup and login
| Select SignUp	| Email, Username & Password	| Redirect to login
| Select Login	| Username & password | Redirect to page with app pitches based on categories & commenting section
| Select comment button	| Comment | Form that you input your comment
| Click on submit |  | Redirect to all comments tamplate with your comment & other comments

# Development Installation

To get the code:

1. Clone the Repository

https://github.com/jerushaotieno/pitches.git

2. Move to the folder and install requirements

cd pitch-world
pip install -r requirements.txt

3. Export Configurations

export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

4. Run the application
python3.6 manage.py server

5. Test the application
python3.6 manage.py test

6. Open the application on your browser 127.0.0.1:5000.

# Technology Used

* Python3.6
* Flask
* Heroku
* Bootstrap

# Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

# Contact Information

If you have any question or contributions, please email: jerushaotienocoding@gmail.com 

# License

MIT License:

# Copyright 

Copyright (c) 2022 Jerusha Otieno 
