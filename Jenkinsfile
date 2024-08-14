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
                sshagent(['myname-key']) {  // Use the ID assigned in Jenkins for the SSH credentials
                    sh 'chmod +x deploy.sh'
                    sh 'scp -o StrictHostKeyChecking=no deploy.sh ubuntu@34.213.162.58:/home/ubuntu/deploy'
                    sh 'ssh -o StrictHostKeyChecking=no ubuntu@34.213.162.58 "bash /home/ubuntu/deploy/deploy.sh"'
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
