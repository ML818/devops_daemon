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

---

### Continuous Integration -- CI

### Continuous Delivery -- CD

---

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
 
## KVM

### Prerequisition
[check it](https://christitus.com/vm-setup-in-linux/)

---

## Tools Online
### Compiler
[Programiz](https://www.programiz.com/python-programming/online-compiler/)

### Json Editor
[json editor online](https://jsoneditoronline.org/#left=local.nadupu&right=local.jagilu)

### YAML Editor
[YAML editor online](https://codebeautify.org/yaml-editor-online)


---

## Network

#### tcpdump

```bash
# 
tcpdump -i eth01 icmp and host <ip> -nn -c 10 -w ping.pcap
```

---

## Container

### Docker

#### Installaiton

[Official Website Docs Reference](https://docs.docker.com/engine/install/)

Also you can check some mirror sites which would describe the installation of docker.
[ustc-mirrors](https://mirrors.ustc.edu.cn/help/docker-ce.html) 
[tsinghua-mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)

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



```

#### Dockerfile
> Build a custom image from Dockerfile with `docker build -t <image_name> <Dockerfile_path>`















---

# Little Projects

## Wordpress Established

> Based on Ubuntu or Debian
[reference](https://ubuntu.com/tutorials/install-and-configure-wordpress#1-overview)
