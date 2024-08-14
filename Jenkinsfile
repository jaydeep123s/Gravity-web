pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/jaydeep123s/Gravity-web.git'
            }
        }

        stage('Build') {
            steps {
                sh 'chmod +x build.sh'
                sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                sh 'chmod +x test.sh'
                sh './test.sh'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Starting deployment...'
                    // Ensure the local deploy.sh script is executable
                    sh 'chmod +x deploy.sh'
                    echo 'Running SCP...'
                    // Copy the deploy.sh script to the remote server
                    sh 'scp -o StrictHostKeyChecking=no deploy.sh ubuntu@34.213.162.58:/home/ubuntu/deploy'
                    echo 'Running SSH...'
                    // Execute the deploy.sh script on the remote server
                    sh 'ssh -o StrictHostKeyChecking=no ubuntu@34.213.162.58 "cd /home/ubuntu/deploy && ./deploy.sh"'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
