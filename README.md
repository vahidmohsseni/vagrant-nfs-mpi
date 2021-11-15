# Vagrant + NFS + MPI
A simple tutorial for clustering using Vagrant with an application on NFS and MPICH


## MPI codes and section will be added shortly after TEST


## What is Vagrant?
> **Vagrant** is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.

## What is NFS?
> **Network File System** (NFS) is a distributed file system protocol, allowing a user on a client computer to access files over a computer network much like local storage is accessed.

## What is MPI and MPICH?
> **Message Passing Interface** (MPI) is a standardized and portable message-passing standard designed to function on parallel computing architectures. 

> **MPICH** is a high-performance and widely portable implementation of the Message Passing Interface (MPI)

## Installation 
The porocess of installation on your system (host) is simple.

### Install Vagrant

#### Ubuntu-based OS
```shell
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install vagrant
```
#### Windows and Other OSs
Just follow the instrution on **[Vagrant Installation Page](https://www.vagrantup.com/downloads "Vagrant Installation Page")**.

### Install VirtualBox

#### Ubuntu-based OS
```shell
sudo apt install virtualbox
```

#### Windows and Other OSs
Download and install from this **[link](https://www.virtualbox.org/wiki/Downloads)**


## Run and Connect to VMs
You can easily have a cluster with 3 nodes by running the following command. 
```shell
git pull https://github.com/vahidmohsseni/vagrant-nfs-mpi
cd vagrant-nfs-mpi
vagrant up
```

To ssh and Connect to VM
```shell
vagrant ssh [name of the VM]
```

To stop VMs
```shell
vagrant halt [name of specific VM]
```

To delete VMs
```shell
vagrant destory [name of specific VM]
```



