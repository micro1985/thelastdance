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
                sh 'python sys.py'
            }
        }
        stage('Test') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh 'python test.py'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'cat ./index.html'
            }
        }
    }
}
