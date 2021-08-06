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
            }
        }
        
        stage('Build') {
            steps {
                sh 'python sys.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python test.py'
            }
        }
        stage('Deploy') {
          steps {
	    withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS_Creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
    		  sh '''
		  echo "--------------------------Destroying Terraform---------------------------"
                  terraform destroy -auto-approve
		  echo "--------------------------Initialising Terraform-------------------------"
                  terraform init
		  echo "--------------------------Planinging Terraform--------------------------"
		  terraform plan
		  echo "--------------------------Applying Terraform----------------------------"
                  terraform apply -auto-approve
		  '''
		}
            }
        }
    }
}
