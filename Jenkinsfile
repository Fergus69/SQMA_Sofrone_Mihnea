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
                // Use 'pip install' to get the reporting library
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Execute Tests') {
            steps {
                script {
                    echo "Running tests: ${params.TEST_SELECTION}"
                    // This now generates XML files in /test-reports folder
                    bat "python3 run_tests.py ${params.TEST_SELECTION}"
                }
            }
        }
    }

    post {
        always {
            // This tells Jenkins to look for XML files and create the UI Report
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
