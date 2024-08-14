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
                    withCredentials([file(credentialsId: '34.213.162.58', variable: 'SSH_KEY')]) {
                        sh 'chmod +x deploy.sh'
                        echo 'Running SCP...'
                        sh "scp -i ${SSH_KEY} -o StrictHostKeyChecking=no deploy.sh ubuntu@34.213.162.58:/home/ubuntu/deploy"
                        echo 'Running SSH...'
                        sh "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no ubuntu@34.213.162.58 'cd /home/ubuntu/deploy && ./deploy.sh'"
                    }
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
