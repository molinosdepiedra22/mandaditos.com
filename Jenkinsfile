pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                echo 'Clonando repositorio...'
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat 'py -m pip install -r requeriments.txt'
            }
        }

        stage('Verificar configuracion Django') {
            steps {
                bat 'py manage.py check'
            }
        }

        stage('Aplicar migraciones') {
            steps {
                bat 'py manage.py migrate --noinput'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat 'py manage.py test pedidos --verbosity=2'
            }
        }

    }

    post {
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline fallo. Revisar logs.'
        }
    }
}