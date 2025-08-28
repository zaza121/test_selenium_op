pipeline {
    agent any

    stages {
        stage('Install pipx') {
            steps {
                sh 'apt update'
                sh 'apt install -y python3 python3-pip python3-venv pipx'
            }
        }
        stage('Prepare Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    // Activate the virtual environment
                    sh '. venv/bin/activate'
                    // Install Selenium into the virtual environment
                    sh 'pip install --break-system-packages selenium'
                    sh 'pip install --break-system-packages pytest'
                }
            }
        }
        stage('Run test') {
            steps {
                script {
                    // Create a virtual environment
                    // sh 'python3 -m venv venv'
                    // Activate the virtual environment
                    // sh '. venv/bin/activate'
                    // Install Selenium into the virtual environment
                    // sh 'pwd'
                    sh 'pytest'
                }
            }
        }
    }
}
