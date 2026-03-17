pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Oviya1127/sre-project.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Build successful"'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                scp -r * ubuntu@<YOUR_SERVER_IP>:/var/www/myapp/

                ssh ubuntu@<YOUR_SERVER_IP> "
                cd /var/www/myapp &&
                sudo systemctl restart nginx
                "
                '''
            }
        }
    }
}
