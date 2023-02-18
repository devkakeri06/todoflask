# todoflask

Prerequisites
Python 3 or higher installed on your computer.
Flask framework installed in Python. You can install Flask by running the following command in your terminal/command prompt:
Copy code
pip install flask
Running the Flask app
To run your Flask application from VS Code, follow these steps:

Open VS Code and navigate to the folder where your Flask app is located. You can do this by clicking File > Open Folder and selecting the folder containing your Flask app.

Open a new terminal in VS Code by going to the Terminal menu and selecting New Terminal or by pressing `Ctrl+Shift+``.

If you are using a virtual environment for your Flask app, activate it by running the following command:

bash
Copy code
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
This will activate the virtual environment and allow you to run your Flask app with the correct dependencies.

Set the FLASK_APP environment variable to the name of your Flask app's entry point file. This is usually app.py or main.py. You can set the environment variable by running the following command:

bash
Copy code
export FLASK_APP=app.py  # Linux/Mac
set FLASK_APP=app.py     # Windows
This tells Flask which file to use as the entry point for your app.

(Optional) Set the FLASK_ENV environment variable to development to enable debug mode. Debug mode is useful for development because it provides helpful error messages in the browser. You can set the environment variable by running the following command:

bash
Copy code
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows
Run the Flask app by running the following command:

Copy code
flask run
This will start the Flask development server and your app will be accessible at http://localhost:5000 in your web browser.

Note: If you want to use a different port number, you can specify it by running flask run --port=8080, for example.

Once you're done running your Flask app, you can stop the development server by pressing Ctrl+C in the terminal.
