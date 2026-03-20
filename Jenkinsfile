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
stage('Deploy to Server2') {
    steps {
        sh '''
        scp -i /var/lib/jenkins/sre.pem -o StrictHostKeyChecking=no -r \
        Jenkinsfile README.md __pycache__ app.py requirements.txt templates \
        ubuntu@44.202.226.195:/home/ubuntu/

        ssh -i /var/lib/jenkins/sre.pem -o StrictHostKeyChecking=no ubuntu@44.202.226.195 << 'EOF'
        sudo mv /home/ubuntu/* /var/www/html/
        EOF
        '''
    }
}
        }
    }
}
