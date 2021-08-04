pipeline {
    agent any
    
    options {
		timestamps()
	}
	
    stages {
        stage('Checkout GitHub') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/micro1985/thelastdance.git']]])
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo "Stage 1"'
            }
        }
        stage('Test') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'echo "Stage 2"'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Stage 3"'
            }
        }
    }
}
