pipeline {

    agent none 
    
    triggers {
        cron('H 3 * * *')
    }

    stages {
        stage('Build') {
            agent {
                docker { image 'python:3.11-slim' }
            }
            steps {
                echo 'Simulando build/compilação do código Python...'
                sh 'python -m py_compile app.py'
            }
        }
        
        stage('Testes Isolados') {
            agent {
                docker { image 'python:3.11-slim' }
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