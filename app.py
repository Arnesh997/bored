from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_activities', methods=['POST'])
def generate_activities():
    url = 'http://www.boredapi.com/api/activity/'
    activities = []
    
    for _ in range(10):
        response = requests.get(url)
        json_data = response.json()
        activity = json_data['activity']
        activities.append(activity)
    
    return render_template('activities.html', activities=activities)

if __name__ == '__main__':
    app.run(debug=True)
