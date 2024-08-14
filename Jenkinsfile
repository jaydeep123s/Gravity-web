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
                    withCredentials([file(credentialsId: 'myname-key', variable: 'SSH_KEY')]) {
                        // Ensure the deploy.sh script is executable
                        sh 'chmod +x deploy.sh'
                        echo 'Running SCP...'
                        // Copy the deploy.sh script to the remote server
                        sh "scp -i ${SSH_KEY} -o StrictHostKeyChecking=no deploy.sh ubuntu@34.213.162.58:/home/ubuntu/deploy"
                        echo 'Running SSH...'
                        // Execute the deploy.sh script on the remote server
                        sh "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no ubuntu@34.213.162.58 'sudo chmod +x /home/ubuntu/deploy/deploy.sh && sudo /home/ubuntu/deploy/deploy.sh'"
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
