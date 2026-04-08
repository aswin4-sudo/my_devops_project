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
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('SonarCloud Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('sonarcloud') {
                        sh """
                        ${scannerHome}/bin/sonar-scanner \
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

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aswinmeachur/my-app:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push aswinmeachur/my-app:latest'
                }
            }
        }

        // 🔥 NEW STAGE (VERY IMPORTANT)
        stage('Deploy to EC2-2 using Ansible') {
            steps {
                sh '''
                cd ansible
                ansible-playbook -i inventory.ini deploy.yml
                '''
            }
        }
    }
}             
