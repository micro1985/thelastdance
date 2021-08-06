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
    }
	
    stages {
        stage('Checkout GitHub') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/micro1985/thelastdance.git']]])
		sh 'ls -la'
            }
        }
        
        stage('Build') {
            steps {
                sh 'python sys.py'
		sh 'ls -la'
            }
        }
        stage('Test') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh 'python test.py'
		    sh 'ls -la'
                }
            }
        }
        stage('Deploy') {
          steps {
	    withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS_Creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
    		  sh '''
		  echo "============================Testing============================="
		  ls -la
		  echo "Initialising Terraform"
                  terraform init
		  echo "============================Testing============================="
		  ls -la
		  echo "============================Testing============================="
		  echo "Planinging Terraform"
		  terraform plan
		  echo "============================Testing============================="
		  ls -la
		  '''
		}
            }
        }
    }
}
