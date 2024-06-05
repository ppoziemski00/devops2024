pipeline {
    agent any

    environment {
        REPO = 'https://github.com/ppoziemski00/devops2024.git'
        BRANCH = 'main'
        DOCKER_IMAGE = 'bmi-image'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${BRANCH}", url: "${REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("${env.DOCKER_IMAGE}").run("-d -p 5000:5000 --name bmi-container")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sleep 10 // Czekaj na uruchomienie kontenera
                    def response = bat(script: '''
                        powershell -Command "$headers = @{ 'Content-Type' = 'application/json' }; $body = '{\\"weight\\": 70, \\"height\\": 1.75}'; try { $response = Invoke-RestMethod -Uri 'http://localhost:5000/bmi' -Method Post -Headers $headers -Body $body; Write-Output $response } catch { $errorMsg = $_.Exception.Message; Write-Output 'Error Message:' $errorMsg; if ($_.Exception.Response -ne $null) { $statusCode = $_.Exception.Response.StatusCode.value__; $statusDescription = $_.Exception.Response.StatusDescription; Write-Output 'Status Code:' $statusCode; Write-Output 'Status Description:' $statusDescription; $stream = [System.IO.StreamReader]::new($_.Exception.Response.GetResponseStream()); $errorResponse = $stream.ReadToEnd(); Write-Output $errorResponse; } else { Write-Output 'No response from server'; } }"
                    ''', returnStdout: true).trim()
                    echo "Response: ${response}"
                    if (!response.contains('bmi')) {
                        error "Test failed with response: ${response}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        failure {
            emailext (
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) failed",
                body: "Napotkano błędy, sprawdź konsolę.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }

        success {
            emailext (
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) succeeded",
                body: "Proces przebiegł pomyślnie, nie napotkano błędów.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
}
