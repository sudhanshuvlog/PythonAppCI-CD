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
            sh "docker rm -f webos"
            sh "docker pull jinny1/gfgdevops20flask"
            sh "docker run -dit --name webos -p 80:80 jinny1/gfgdevops20flask"
        }
    }
}
}