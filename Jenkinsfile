 pipeline{
    agent any
    stages{
        stage('Start'){
            steps{
                echo 'Pipeline started'
                ech 'This is test branch'
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