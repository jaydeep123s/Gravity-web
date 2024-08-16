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
            withCredentials([sshUserPrivateKey(credentialsId: '54.184.219.225', keyFileVariable: 'SSH_KEY', usernameVariable: 'USER')]) {
                // Ensure deploy.sh is executable
                sh 'chmod +x deploy.sh'
                
                // Echo SSH key and user for debugging purposes
                echo "SSH Key: ${SSH_KEY}"
                echo "User: ${USER}"
                
                // Copy deploy.sh to the target server
                echo 'Running SCP...'
                sh "scp -i ${SSH_KEY} -o StrictHostKeyChecking=no deploy.sh ${USER}@54.184.219.225:/home/${USER}/deploy/"
                
                // Check if the file was copied successfully
                echo 'Checking if deploy.sh was copied...'
                sh "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no ${USER}@54.184.219.225 'ls -la /home/${USER}/deploy/'"
                
                // Execute the deploy.sh script on the target server
                echo 'Running SSH...'
                sh "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no ${USER}@54.184.219.225 'mkdir -p /home/${USER}/deploy && cd /home/${USER}/deploy && ./deploy.sh'"
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
