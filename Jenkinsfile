pipeline {
//Update the custom docker agent in Jenkins file in the below section
  agent any

  stages {

    stage('Setup') {
         steps {

         script {
                    def workspace = pwd()
                    echo "My workspace is ${workspace}"
                    echo "Setting up the workspace"
                 }
                 }
          }

    stage('Checkout code'){
        steps {
           echo  "Pulling Branch from Github"
           checkout([$class: 'GitSCM',
           branches: [[name: '*/master']],
           doGenerateSubmoduleConfigurations: false,
           extensions: [],
           submoduleCfg: [],
          
        }
    }

    stage('Installing tools'){
        steps {
                echo "Installing tools is performed"
        }
    }

     stage('Installing requirements'){
        steps {
                echo "Installing requirements is performed"
          }
        }
    }

     stage('Compile code'){
        steps {
                echo "Compile code is performed"
           }
        }
    }

      stage('Test with pytest') {
           steps {
                  echo "pytest is successful"
           }
           }
         }


           

  }

  }
