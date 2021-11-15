# Start Configuration of the Machines with shell scripts

# Run this command within shell provision
# You should pass the args: ["username"]
# Syntax mentioned in server
$addUserScript = <<SCRIPT
adduser --disabled-password --gecos "" $1
usermod -aG sudo $1
mkdir /home/$1/.ssh
chmod 700 /home/$1/.ssh
chown $1 /home/$1/.ssh
chgrp $1 /home/$1/.ssh
cp .ssh/authorized_keys /home/$1/.ssh/
chown $1 /home/$1/.ssh/authorized_keys
chgrp $1 /home/$1/.ssh/authorized_keys
SCRIPT


# Activate ssh login with password
# To change default password following config
# config.ssh.password "my strong password"
# config.ssh.dsa_authentication = false # default value is true
$activatePasswordAuth = <<SCRIPT
sed -i "s/PasswordAuthentication/# PasswordAuthentication/g" /etc/ssh/sshd_config
echo PasswordAuthentication yes >> /etc/ssh/sshd_config
systemctl restart sshd
SCRIPT


# Install Network File System (NFS) on server
$installNFSServer = <<SCRIPT
apt install nfs-kernel-server -y
mkdir -p /mnt/mirror
chown -R nobody:nogroup /mnt/mirror
chmod 777 /mnt/mirror/
sed -i -e '$a/mnt/mirror 192.168.10.0/24(rw,sync)' /etc/exports
exportfs -a 
systemctl restart nfs-kernel-server.service
SCRIPT


# Install NFS on clients
$installNFSClient = <<SCRIPT
apt install nfs-common -y
mkdir -p cmirror
mount 192.168.10.2:/mnt/mirror cmirror
touch cmirror/file.txt
echo hello >> cmirror/file.txt
SCRIPT


# Install MPICH
# Commands goes here!



# Creatign VARIABLES 
VM1 = "server"
VM2 = "client1"
VM3 = "client2"

ServerIP  = "192.168.10.2"
Client1IP = "192.168.10.3"
Client2IP = "192.168.10.4"


Vagrant.configure("2") do |config|

  config.vm.define VM1 do |server|

    # creating a vm from base image
    server.vm.box = "ubuntu/bionic64"
    server.vm.hostname = VM1

    server.vm.network "private_network", ip: ServerIP, hostname: true

    # Add new sudoer user
    # server.vm.provision "AddSudoUser", type: "shell", run: "once", inline: #addUserScript, args: ["server"]
    
    # CAUTION: unconmmenting following line results is enabling password login
    # server.vm.provision "sshPassAuth", type: "shell", run: "once", inline: $activatePasswordAuth

    # Install NFS on server
    server.vm.provision "InstallServerNFS", type: "shell", run: "once", inline: $installNFSServer

    # Copy files into server
    server.vm.provision "copyServerPy", type: "file", source: "socket_test/server.py", destination: "/home/vagrant/", run: "always"


  end






  config.vm.define "client1" do |client1|

    client1.vm.box = "ubuntu/bionic64"
    client1.vm.hostname = VM2

    client1.vm.network "private_network", ip: Client1IP, hostname: true


    # Install NFS on client
    client1.vm.provision "InstallClientNFS", type: "shell", run: "once", inline: $installNFSClient

    # Mount NFS Folder after reboot every time
    # Also you can add following line at /etc/fstab but not recommended.
    # 192.168.10.2:/mnt/mirror    /home/vagrant/cmirror   nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
    client1.vm.provision "MountNFS", type: "shell", run: "always", inline: "mount 192.168.10.2:/mnt/mirror cmirror"

    # Copy files into client
    client1.vm.provision "copyClientPy", type: "file", source: "socket_test/client.py", destination: "/home/vagrant/", run: "always"



  end
  


end
