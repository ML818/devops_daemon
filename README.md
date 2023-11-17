# devops_daemon

### Processes
1. Requirment gathering
2. Planning
3. Designing
4. Development
5. Testing
6. Deploy & Maintain

#### Models in SDLC
- Waterfall
- Agile
	1. code changes
	2. Deploy
	3. Test/QA


---

### AWS
- IAM
- CloudWatch
- Certificate Manager
- Billing

#### Operations
- EC2

---

### Continuous Integration -- CI

### Continuous Delivery -- CD

---

## Virtualization

### Vagrant
> **Virtual Machines Management Tool**

#### Creating VM
> 1. Create a specific directory for the VM which you want to create.
`mkdir /path/to/someOS`

> 2. View the [vagrant cloud](https://app.vagrantup.com/boxes/search), choose the package you want, and check the `Vagrantfile` of the package, particularly `config.vm.box = "ubuntu/jammy64"`, use the value to initial the VM. 

> 3. Change into the specific directory and initial VM. 
- `cd /path/to/someOS`
- `vagrant init ubuntu/jammy64`
	- it will **generate** `Vagrantfile` automatically in the directory.
	- You can change the configuration in `Vagrantfile` if you want.

> 4. Finished Step-3. **create** and **boot** the VM.
`vagrant up`

#### Manage VM
```bash
# check the VM status.
$ vagrant status
Current machine states:

default                   running (virtualbox)

# check all VMs status
$ vagrant global-status
id       name    provider   state    directory
-------------------------------------------------------------------------------
4ad6393  default virtualbox poweroff C:/Users/Administrator/vagrant-vms/centos
4c62fac  default virtualbox running  C:/Users/Administrator/vagrant-vms/ubuntu

# Check local packages
$ vagrant box list
eurolinux-vagrant/centos-stream-9 (virtualbox, 9.0.31)
ubuntu/jammy64                    (virtualbox, 20231012.0.0)

# boot VM, if the VM is not existed, it will create and boot
$ vagrant up

# reboot VM
$ vagrant reload

# shut down VM
$ vagrant halt

# delete VM
$ vagrant destroy

# Connect to VM by ssh
$ vagrant ssh

#
```
---

### KVM
#### Prerequisition
[check it](https://christitus.com/vm-setup-in-linux/)

---

### Proxmox
> A virtual machine platform
> It can create VMs and containers

#### Templates
##### Create Templates
> The operation of VM and container are almost the same as each other.
1. Remove `/etc/ssh/ssh_host_*`
2. Clean the machine_id : `sudo truncate -s 0 /etc/machine_id`, if the host does not have this file, ignore this step.
3. Poweroff and convert to template

##### Create instances by template
- After the instance boot, it needs to execute `sudo dpkg-reconfigure openssh-server`, refresh ssh keys.

---
## Some Online Tools

### Json Editor
[json editor online](https://jsoneditoronline.org/#left=local.nadupu&right=local.jagilu)

### YAML Editor
[YAML editor online](https://codebeautify.org/yaml-editor-online)

### Shell Guide
[ExplainShell](https://explainshell.com/)

---

## Network

#### tcpdump

```bash
# catch network packs
# -i -- ethernet interface
# icmp -- protocol
# host <ip> -- target
# -c -- limit the number of packs
# -nn -- don't analyze IP and port 
# -w -- output a file with its name
tcpdump -i eth01 icmp and host <ip> -nn -c 10 -w ping.pcap
```

---

## Container

### Docker

#### Installaiton

[Official Website Docs Reference](https://docs.docker.com/engine/install/)

Also you can check some mirror sites which would describe the installation of docker.
- [ustc-mirrors](https://mirrors.ustc.edu.cn/help/docker-ce.html) 
- [tsinghua-mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)

#### Operations
```bash
# Check local images
docker images

# Remove image
docker rmi <image_name>

# Check processes of docker containers
# -a which means all processes, even containers had exited.
docker ps <-a>

# Create and run container by specific image
# -d running this container in the background.
# -p setup forward of port between local and container.
docker run --name <container_name> -d -p <lcoal_machine_port:container_port> <image_name>

# Check details about specific container
docker inspect <container_name/container_id>

# Delete all things which unused except local images.
docker system prune

# Volume Operations
## Check volumes info
docker volume ls

## Create volume
docker volume create <volume-name>

## Remove volume
docker volume rm <volume-name>

## Remove all volumes
docker volume prune
```
> **Notice** : Remove container and remove volume is **separate step**. If you use volumes in a container, remove the container will not remove the volumes at the same time.


#### Dockerfile
> Build a custom image from Dockerfile with the command below.
`docker build -t <image_name> <Dockerfile_path>`


#### Docker Compose
> Build clusters by a YAML file.
- All configurations in compose YAML file.

##### YAML File
> Example
```yaml
services:
  app:
    image: node:18-alpine
    command: sh -c "yarn install && yarn run dev"
    ports:
      - 127.0.0.1:3000:3000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos

  mysql:
    image: mysql:8.0
    volumes:
      - todo-mysql-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: todos

volumes:
  todo-mysql-data:
```

##### Operations of Compose
- Run: `docker compose up -d`
- Stop: `docker compose down`



---

## Microservices

---

## Maven

> Java projects

### Operations
1. Install openjdk-11-jdk and maven
2. Locate in work directory which must have `pom.xml`
3. `mvn validate`
4. `mvn test`
5. `mvn clean`
6. `mvn install`

---

## CI with Jenkins

- Open source
- Extensible

##### Prerequisite
> Java, JRE, JDK

### Jenkins in Linux
[reference from official website](https://www.jenkins.io/doc/book/installing/linux/)

### Jenkins in Docker
> Customize the official Jenkins Docker image, by executing the following two steps:
1. Create a `Dockerfile` with the following content:
``` Dockerfile
FROM jenkins/jenkins:2.414.3-jdk17
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
    https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
    signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
    https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
```

> Build a new docker image from this Dockerfile, and assign the image a meaningful name, such as "myjenkins-blueocean:2.414.3-1":
`docker build -t myjenkins-blueocean:2.414.3-1 .`

2. Create a bridge network in Docker
```bash
docker network create jenkins
```

3. Run your own `myjenkins-blueocean:2.414.3-1` image as a container in Docker using the following `docker run` command:
```bash
docker run \
  --name jenkins-blueocean \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.414.3-1 
```

> Then we can check jenkins page with `localhost:8080` in browser.

[Reference](https://www.jenkins.io/doc/book/installing/docker/)

### Pipeline
> Syntax
```groovy
pipeline{
    agent{
        lable "<node_name>"
        }
    tools{
        <key> <value>
        }
    environment{
        <key> = "<value>"
        ...
        }
    stages{
        stage('<describe_operation>'){
            steps{
                <commands>
                ...
                }
            }
            post{
                
                }
        }
}
```
Example of pipeline
```groovy
pipeline {
	agent any
	tools {
		maven "MAVEN3"
		jkd "OpenJDK17"
	}
	stages {
		stage('Fetch code') {
			steps {
				git branch: 'main', url: 'https://github.com/hkhcoder/vprofile-project.git'
			}
		}

		stage('Build') {
			steps {
				sh 'mvn install -DskipTests'
			}
			post {
				success {
					echo 'Archiving artifacts now.'
					archiveArtifacts artifacts: '**/*.war'
				}
			}
		}

		stage('Unit Test') {
			steps {
				sh 'mvn test'
			}
		}
	}
}
```
---

### Code Analysis
> Sonarqube
#### Sonarqube in Docker
```shell
docker run -d -p 9000:9000 --name sonar-server -v sonar-data:/var/sonar_home/sonar_data  sonarqube
```
- the embedded database is not good enough

#### Configuration in Jenkins
1. Install plugin **SonarQube Scanner for Jenkins**.
    - `Dashboard` -> `Manage Jenkins` -> `Plugins`
2. Add a authentication token in Sonar server.
    - `My account` -> `Security` -> `Tokens`
    - Filled Name, Type and Expires, then Generate. Remeber store it where you want.
3. Configuration in Jenkins
    - `Dashboard` -> `Manage Jenkins` -> `System` -> `SonarQube servers` -> `Add SonarQube` 
    - Filled Name, Server URL and **Server authentication token**(it is none at the first).
        - After **save** and **refresh** the page, the same way, we can choose the name of token which we created in Sonar server. 


---

# Little Projects

## Wordpress Established

> Based on Ubuntu or Debian
[reference](https://ubuntu.com/tutorials/install-and-configure-wordpress#1-overview)
