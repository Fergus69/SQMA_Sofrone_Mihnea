pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SELECTION', 
            choices: ['All', 'TestOne', 'TestTwo'], 
            description: 'Choose which Test Suite to run'
        )
    }

    stages {
        stage('Setup') {
            steps {
                echo "Installing Python dependencies..."
                // Folosim calea completa catre python.exe
                bat '"C:\\Users\\sofro\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Execute Tests') {
            steps {
                script {
                    echo "Running tests: ${params.TEST_SELECTION}"
                    // Aici era greseala cu 'python3'. Am pus calea completa.
                    bat '"C:\\Users\\sofro\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" run_tests.py %TEST_SELECTION%'
                }
            }
        }
    }

    post {
        always {
            junit 'test-reports/*.xml'
        }
        success {
            echo 'SUCCESS: Tests passed.'
        }
        failure {
            echo 'FAILURE: Tests failed.'
        }
    }
}
