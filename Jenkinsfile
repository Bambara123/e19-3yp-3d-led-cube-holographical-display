pipeline {
  agent any
  stages {
    stage('Checkout code') {
      steps {
        git(url: 'https://github.com/Bambara123/e19-3yp-3d-led-cube-holographical-display', branch: 'main')
      }
    }

    stage('shell script') {
      steps {
        sh 'dir'
      }
    }

  }
}