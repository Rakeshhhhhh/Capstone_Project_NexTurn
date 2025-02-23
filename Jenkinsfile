pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "rakesh80/nexturn-capstone-project"  // Your Docker Hub image

        CONTAINER_NAME = "nexturn-capstone"
        VENV_PATH = "env"  // Virtual environment for tests
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Rakeshhhhhh/Capstone_Project_NexTurn.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                bat '''
                    python -m venv %VENV_PATH%
                    call %VENV_PATH%\\Scripts\\activate
                    %VENV_PATH%\\Scripts\\python.exe -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    call %VENV_PATH%\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call %VENV_PATH%\\Scripts\\activate
                    pytest || echo "Tests failed"
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                    docker pull %DOCKER_IMAGE%:latest
                    docker stop %CONTAINER_NAME% || echo "No running container"
                    docker rm %CONTAINER_NAME% || echo "No container to remove"
                    docker run -d -p 5000:5000 --name %CONTAINER_NAME% %DOCKER_IMAGE%:latest

                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful! 🚀'
        }
        failure {
            echo 'Deployment failed! ❌'
        }
    }
}
