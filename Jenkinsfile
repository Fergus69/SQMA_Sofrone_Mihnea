pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo "Pregatim mediul..."
                // Instalam dependintele o singura data
                bat '"C:\\Users\\sofro\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Full Regression') {
            // Aici e magia: "parallel" ruleaza ambele teste simultan!
            parallel {
                stage('Test Suite One') {
                    steps {
                        echo "Running Suite 1..."
                        // Rulam doar primul set de teste
                        bat '"C:\\Users\\sofro\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" run_tests.py TestOne'
                    }
                }

                stage('Test Suite Two') {
                    steps {
                        echo "Running Suite 2..."
                        // Rulam doar al doilea set de teste
                        bat '"C:\\Users\\sofro\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" run_tests.py TestTwo'
                    }
                }
            }
        }
    }

    post {
        always {
            // Colectam rapoartele de la ambele teste
            junit 'test-reports/*.xml'
        }
        success {
            echo 'GREAT SUCCESS: Toate testele au trecut!'
        }
        failure {
            echo 'FAIL: Unul dintre teste a picat.'
        }
    }
}
