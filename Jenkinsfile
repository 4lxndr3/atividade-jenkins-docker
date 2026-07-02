pipeline {
    agent none 
    
    triggers {
       cron('* * * * *')
    }

    stages {
        stage('Build') {
            agent {
                docker { 
                    image 'python:3.11-slim' 
                    args '-u root' 
                }
            }
            steps {
                echo 'Simulando build/compilação do código Python...'
                sh 'python -m py_compile app.py'
            }
        }
        
        stage('Testes Isolados') {
            agent {
                docker { 
                    image 'python:3.11-slim' 
                    args '-u root' 
                }
            }
            steps {
                echo 'Instalando dependências de teste...'
                sh 'pip install -r requirements.txt'
                
                echo 'Executando testes...'
                sh 'pytest test_app.py --junitxml=results.xml || true'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }
}