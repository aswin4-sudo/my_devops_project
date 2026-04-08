pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aswin4-sudo/my_devops_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('SonarCloud Analysis') {
            steps {
                sh """
                sonar-scanner \
                -Dsonar.projectKey=aswin4-sudo_my_devops_project \
                -Dsonar.organization=aswin4-sudo \
                -Dsonar.sources=. \
                -Dsonar.host.url=https://sonarcloud.io \
                -Dsonar.login=$SONAR_TOKEN
                """
            }
        }
    }
}
