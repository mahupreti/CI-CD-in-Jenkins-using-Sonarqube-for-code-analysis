pipeline {
  agent any
  
  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    
    stage('Unit test') {
      steps {
        sh 'python manage.py test'
      }
    }
    
    stage('Build') {
      steps {
        sh 'python manage.py makemigrations'
        sh 'python manage.py migrate'
      }
    }
   stage('Code analysis'){
       environment {
            scannerHome = tool "sonarscanner"
        }
        steps{
        echo "sonar code here"
        
        withSonarQubeEnv("sonarserver") {  
            sh '''${scannerHome}/bin/sonar-scanner \
                -Dsonar.projectKey=jenkins-first-test \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://localhost:9000 \
                -Dsonar.login=sqp_6a88193d0d6a491af3431dfe1aed86c98f4164ba \
                -Dsonar.python.coverage.reportPaths=/jenkins-first-test/coverage.xml \
                -Dsonar.python.xunit.reportPath=/jenkins-first-test/result.xml \
                -Dsonar.coverage.dtdVerification=false \
                -Dsonar.inclusions=app.py \
                -Dsonar.coverage.exclusions=**/__init__.py''' 
        }         
     }  
}
    
    stage('Deploy') {
      steps {
        sh 'python manage.py runserver'
      }
    }
  }
}
