pipeline {
    agent any
    
    options { timestamps() }
	
    tools {
        "org.jenkinsci.plugins.terraform.TerraformInstallation" "terraform"
    }
    environment {
        TF_HOME = tool('terraform')
        TF_IN_AUTOMATION = "true"
        PATH = "$TF_HOME:$PATH"
	AWS_ACCESS_KEY_ID = "$AWS_ACCESS_KEY_ID"
	AWS_SECRET_ACCESS_KEY = "$AWS_SECRET_ACCESS_KEY"
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
                sh '''
		echo "Initialising Terraform"
                terraform init
		echo "Planinging Terraform"
		terraform plan
		'''
            }
        }
    }
}
