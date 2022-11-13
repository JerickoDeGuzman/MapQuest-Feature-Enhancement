node {
   stage('Preparation') {
       catchError(buildResult: 'SUCCESS') {
          sh 'docker stop mapquestapprunning'
          sh 'docker rm mapquestapprunning'
       }
   }
   stage('Build') {
       build 'BuildAppJobMapquest'
   }
   stage('Results') {
       build 'TestAppJobMapquest'
   }
}
