# Eye Art System

## Overview
The Eye Art System is an innovative application that allows users with limited mobility to create virtual artwork using eye movements. By leveraging MediaPipe Iris for eye tracking and Pygame for drawing, this system provides an accessible and creative outlet for expression.

## Features
- Eye tracking using MediaPipe Iris
- Drawing capabilities controlled by eye movements
- User-friendly interface built with Pygame

## Project Structure
```
eye-art-system
├── src
│   ├── main.py          # Entry point of the application
│   ├── eye_tracking.py   # Eye tracking functionality
│   ├── drawing.py        # Drawing surface management
│   └── utils
│       └── __init__.py   # Utility functions and constants
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/eye-art-system.git
   ```
2. Navigate to the project directory:
   ```
   cd eye-art-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/main.py
   ```
2. Follow the on-screen instructions to start creating art using your eye movements.

## Dependencies
- `mediapipe`
- `pygame`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
