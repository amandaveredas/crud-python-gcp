pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '0c1ae178-c4ae-429e-83ab-85ceae8d3f89', url: 'https://github.com/amandaveredas/crud-python-gcp.git']]])    
            }

        }

        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '0c1ae178-c4ae-429e-83ab-85ceae8d3f89', url: 'https://github.com/amandaveredas/crud-python-gcp.git'
            }
        }

        stage('Production') {
            steps {
                //sh "arquivo de teste"
                echo 'The job has been put in production '
            }
        }
    }
}