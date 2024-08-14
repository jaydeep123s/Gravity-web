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
                sshagent(['myname']) {
                    sh 'ssh -o StrictHostKeyChecking=no ubuntu@34.213.162.58 "bash -s" < deploy.sh'
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

