PROJET 7 - Grandpy bot

******************************************************

This project is part of the Openclassroom's Python Developer path. Have a look at https://openclassrooms.com/fr/paths for more information.

Grandpy is a bot developed in Python, which asks a user for a question about a location. It gives back the address and a bit of history about that place, well, you know, like grandpas usually do.

You have two ways for using the created website :
- The fast and easy way. Go to this adress in your internet browser :
    https://oc-projet7-matthiasgil.herokuapp.com/
- The slow way. 
    1) You have to fork the repository and clone it with git.
    Or you can download the full project here at github.
    2) Install the dependencies in your environment using 'pipenv install' and run it using 'pipenv run flask run' to activate a virtual server.
    3) In your internet browser, go to this adress : localhost/5000. You have now access to the website via your own local server.
    4) Have a look at the exemple.env.txt. It's an example of what you have to declare as environment variables to make the magic happen. API keys are mine, so if you want to use the application on your own local device, you have to use Google Cloud Plateform to obtain API keys instead of mine.

Be carefull : the API key is under restriction. Which means the local server solution might not be able to generate expected results if you ask a question to Grandpy.
Be carefull again : the local environment variables present in the .env file have to be present in the Heroku variables' environment. Otherwise, you'll get an error 500 when opening the website.

Have fun !

******************************************************

Created by Matthias GIL with Python 3, Git, Flask, HTML5, CSS3 and JavaScript, in a virtual environment.
