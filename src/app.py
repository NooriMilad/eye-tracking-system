from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from eye_tracking import EyeTracker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
eye_tracker = EyeTracker()

@app.route('/')
def index():
    return render_template('index.html')

def send_eye_data():
    while True:
        x, y = eye_tracker.get_position()  # Beispielmethode, um Eye-Tracking-Daten zu erhalten
        socketio.emit('eye_data', {'x': x, 'y': y})
        socketio.sleep(0.1)

if __name__ == "__main__":
    socketio.start_background_task(target=send_eye_data)
    socketio.run(app, debug=True)