pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'myapp', url: 'https://github.com/jaydeep123s/Gravity-web.git'
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
                    withCredentials([sshUserPrivateKey(credentialsId: '54.202.220.67', keyFileVariable: 'SSH_KEY', usernameVariable: 'USER')]) {
                        sh 'chmod +x deploy.sh'
                        echo 'Running SCP...'
                        sh "scp -i ${SSH_KEY} -o StrictHostKeyChecking=no deploy.sh ${USER)@54.202.220.67:/home/${USER}/deploy"
                        echo 'Running SSH...'
                        sh "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no ${USER}@54.202.220.67 'cd /home/${USER}/deploy && ./deploy.sh'"
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
