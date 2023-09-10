from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_info():
    # Get current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')
    # Get current UTC time
    current_utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')
    # Define GitHub URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"
    # Create the response JSON
   
    slack_name = "Olawale Onakoya"
    track = "Backend"

    response_data = [{
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200}]
    
    filtered_users = response_data
    

    if slack_name:
        filtered_users = [user for user in filtered_users if user['slack_name'].startswith(slack_name)]

    if track:
        filtered_users = [user for user in filtered_users if user['track'].startswith(track)]

    if not filtered_users:
        return "<h2>No user matched your search</h2>", 200, {'Content-Type': 'text/html'}

    return jsonify(filtered_users), render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app