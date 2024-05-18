pipeline{

agent{
    label "ec2"
}

stages{
    stage("hello world"){
        steps{
            echo "hi jenkins"
        }
    }
    stage(" Deploy the container"){
        steps{
            sh "docker run -dit --name webos -p 80:80 jinny1/gfgdevops20flask"
        }
    }
}
}