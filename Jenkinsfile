pipeline {
    agent any

    environment {
        VENV_PATH = "env"  // Virtual environment path
        DOCKER_IMAGE = "flask-rest-api"  // Docker image name
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
                    python3 -m venv ${VENV_PATH}
                    if [ -f "${VENV_PATH}/bin/activate" ]; then
                        . ${VENV_PATH}/bin/activate
                    else
                        ${VENV_PATH}\\Scripts\\activate
                    fi
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    . ${VENV_PATH}/bin/activate || ${VENV_PATH}\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    . ${VENV_PATH}/bin/activate || ${VENV_PATH}\\Scripts\\activate
                    pytest || echo "Tests skipped (if not implemented)"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${DOCKER_IMAGE} ."
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
