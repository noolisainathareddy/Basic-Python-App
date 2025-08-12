 pipeline{
    agent any
    stages{
        stage('Start'){
            steps{
                echo 'Pipeline started'
            }
        }
        stage('Docker Build'){
            steps{
                script{
                    echo "Started Building python app"
                    sh """
                        export PATH=$PATH:/usr/local/bin
                        docker build -t my-python-app .
                    """

                }
            }
        }
    }
 }