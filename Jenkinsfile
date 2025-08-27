 pipeline{
    agent any
    stages{
        stage('Start'){
            steps{
                echo 'Pipeline started'
                echo 'This is test branch'
                sh "echo ${params.BRANCH_NAME}"

            }
        }
        stage('Docker Build'){
            steps{
                script{
                    echo "Started Building python app"
                    sh """
                        export PATH=$PATH:/Users/sainooli/.docker/bin
                        docker build -t my-python-app .
                    """

                }
            }
        }
    }
 }