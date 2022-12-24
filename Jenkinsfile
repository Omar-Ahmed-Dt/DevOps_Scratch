pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build Completed'
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            echo 'first test completed'
          }
        }

        stage('Test 2') {
          steps {
            echo 'second test completed'
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy Completed'
      }
    }

  }
}