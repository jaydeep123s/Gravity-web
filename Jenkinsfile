pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/ci-cd-pipeline.git'
            }
        }

        stage('Build') {
            steps {
                sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                sh './test.sh'
            }
        }

        stage('Deploy') {
            steps {
                sshagent(['your-ssh-credentials-id']) {
                    sh 'ssh -o StrictHostKeyChecking=no ec2-user@<Web-Server-IP> "bash -s" < deploy.sh'
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
