# Grow Smart

## Project Overview
This project involves developing and deploying a Django-based full-stack web application for green house controlled environment farming. The application includes two main apps: one for data visualization and another for handling sensor data and relay control. The front-end is enhanced using Bootstrap for a modern and responsive UI/UX.

## Table of Contents
- Project Overview
- Features
- Project Structure
- Installation
- Usage
- Contributors
- License

## Features
- **Data Visualization**: Displays sensor data in charts.
- **Sensor Data Handling**: Manages sensor data and relay control.
- **UI**: Enhanced with Bootstrap for a modern look and feel.
- **User Authentication**: Secure login and registration system.
- **Environment Control**: Allows users to set parameters for EC, pH, and humidity.

## Project Structure

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/grow_smart.git
    cd grow_smart
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Use the navigation menu to access different features like Sensors, Relay, and Parameter Settings.
- Log in or register to access user-specific features.

## Contributors
- **Yonas**
- **Dagmawit**


