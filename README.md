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

## Test Socket Connection
To make sure that the connection between clients and server nodes (VMs) is established and works properly, two python programs is written. The program is simple. Note that you should always run **server FIRST**. Moreover, every changes in `socket_test` directory directly affects the codes in VM after the VMs are `up`.

In server-side, it opens a socket binds and listens to port 9000 on server. Following instructions lets you to activate and run the program on the server. The program is multi-threaded which means it can handle multiple clients' connection simultaneously. To stop the server from terminal just use `ctrl+c`.

```shell
vagrant ssh server
python3 server.py
```

In client-side, it tries to establish a connection to server which is available in the address "192.168.10.2:9000". Following instruction helps to run this program.

```shell
vagrant ssh client1
python3 client.py
```