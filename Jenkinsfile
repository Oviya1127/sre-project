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
                scp -r * ubuntu@44.202.226.195:/var/www/myapp/

                ssh ubuntu@44.202.226.195
                cd /var/www/myapp &&
                sudo systemctl restart nginx
                "
                '''
            }
        }
    }
}
