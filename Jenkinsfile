pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON = "C:\\Users\\Deva\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat """
                "%PYTHON%" -m venv %VENV%
                %VENV%\\Scripts\\python -m pip install --upgrade pip
                %VENV%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                bat """
                %VENV%\\Scripts\\pytest
                """
            }
        }
    }

    post {
        success {
            echo "✅ Build & Tests successful"
        }
    }
}
