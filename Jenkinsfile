
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sidra971/cicd-assignment-fa23-bct-043.git'
            }
        }

        stage('Package') {
            steps {
                sh 'docker build -t cicd-selenium-test .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm cicd-selenium-test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker build -t cicd-web-app -f Dockerfile.web .'
                sh 'docker rm -f cicd-web-app || true'
                sh 'docker run -d --name cicd-web-app -p 8081:80 cicd-web-app'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Deployment was not completed.'
        }
    }
}
