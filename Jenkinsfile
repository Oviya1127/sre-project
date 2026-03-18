pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Oviya1127/sre-project.git'
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
                scp -i /var/lib/jenkins/sre.pem -o StrictHostKeyChecking=no -r * ubuntu@44.202.226.195:/var/www/html/

                ssh -i /var/lib/jenkins/sre.pem -o StrictHostKeyChecking=no ubuntu@44.202.226.195 "
                sudo systemctl restart nginx
                "
                '''
            }
        }
    }
}
