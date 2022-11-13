properties([pipelineTriggers([githubPush()])])

node {
    
    git url: 'https://github.com/JerickoDeGuzman/MapQuest-Feature-Enhancement.git',  
    branch: 'main'
    
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