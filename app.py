from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model (replace with your actual model path)
model = joblib.load('linear_regression_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Retrieve form data
            matriculation_marks = float(request.form['matriculation_marks'])
            intermediate_marks = float(request.form['intermediate_marks'])
            age = int(request.form['age'])
            sex = int(request.form['sex'])
            attendance = float(request.form['attendance'])
            study_hours = float(request.form['study_hours'])
            extracurricular_activities = int(request.form['extracurricular_activities'])
            socioeconomic_status = int(request.form['socioeconomic_status'])
            parental_education = int(request.form['parental_education'])
            entrance_exam_scores = int(request.form['entrance_exam_scores'])
            previous_semester_grades = float(request.form['previous_semester_grades'])
            course_load = int(request.form['course_load'])
            class_participation = int(request.form['class_participation'])
            sleep_patterns = float(request.form['sleep_patterns'])
            health = int(request.form['health'])
            access_to_resources = int(request.form['access_to_resources'])
            mentorship_or_tutoring = int(request.form['mentorship_or_tutoring'])

            # Create feature array
            features = np.array([
                matriculation_marks, intermediate_marks, age, sex, attendance, study_hours,
                extracurricular_activities, socioeconomic_status, parental_education,
                entrance_exam_scores, previous_semester_grades, course_load, class_participation,
                sleep_patterns, health, access_to_resources, mentorship_or_tutoring
            ]).reshape(1, -1)

            # Make prediction
            prediction = model.predict(features)
            predicted_cgpa = round(prediction[0], 2)

            return render_template('index.html', predicted_cgpa=predicted_cgpa, error=None)

        except ValueError:
            # Provide a custom error message for value errors
            error_message = "Please enter valid numeric values for all fields."
            return render_template('index.html', predicted_cgpa=None, error=error_message)

        except Exception as e:
            # Log the exception for debugging
            app.logger.error("An error occurred: %s", e)
            error_message = "An error occurred while processing your request."
            return render_template('index.html', predicted_cgpa=None, error=error_message)

    # Render the initial form
    return render_template('index.html', predicted_cgpa=None, error=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
