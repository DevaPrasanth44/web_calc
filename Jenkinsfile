pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON_PATH = "C:\\Users\\Deva\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Creating virtual environment and installing dependencies'
                bat """
                %PYTHON_PATH% -m venv %VENV%
                %VENV%\\Scripts\\python -m pip install --upgrade pip
                %VENV%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests'
                bat "%VENV%\\Scripts\\pytest"
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Starting Flask app in background and opening Chrome'
                bat """
                start /B cmd /c "%VENV%\\Scripts\\python app.py"
                ping 127.0.0.1 -n 6 > nul
                start chrome http://127.0.0.1:5000
                """
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
