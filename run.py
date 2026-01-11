from market import app

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)

#How to run the application:
# 1. Open a terminal or command prompt.
# 2. Navigate to the directory where run.py is located.
# 3. Execute the command: python run.py
# 4. The Flask development server will start, and you can access the application in your web browser at http://localhost:5000
# Note: Ensure that you have Flask and any other dependencies installed in your Python environment.
