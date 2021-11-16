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
mkdir -p /mnt/mirror
mount 192.168.10.2:/mnt/mirror /mnt/mirror
touch /mnt/mirror/file.txt
echo hello >> /mnt/mirror/file.txt
SCRIPT


# Install MPICH
$installMPICH = <<SCRIPT
apt update
apt install mpich -y
SCRIPT


# Declare VARIABLES 

VM1 = "server"

ServerIP  = "192.168.10.2"


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

    # Add temporary private and public key to server
    # CAUTION: The keys should be removed after initial configuration
    server.vm.provision "CopySSHKeys", type: "file", source: "ssh_keys/", destination: "/home/vagrant/"
    server.vm.provision "ConfigSSH", type: "shell", inline: <<-SCRIPT
    cat ssh_keys/id_rsa.pub >> .ssh/authorized_keys
    cp ssh_keys/id_rsa .ssh/.
    chmod 600 .ssh/id_rsa
    chown vagrant:vagrant .ssh/id_rsa
    SCRIPT

    # Install NFS on server
    server.vm.provision "InstallServerNFS", type: "shell", run: "once", inline: $installNFSServer

    # Copy files into server
    server.vm.provision "CopyServerPy", type: "file", source: "socket_test/server.py", destination: "/home/vagrant/", run: "always"

    # Install MPICH
    server.vm.provision "InstallMPICH", type: "shell", run: "once", inline: $installMPICH

    # Copy MPI examples into NFS directory
    server.vm.provision "CopyMPIExample", type: "file", source: "mpi_codes/", destination: "/mnt/mirror/"

  end


  (1..2).each do |i|
    config.vm.define "client#{i}" do |node|
      
      node.vm.box = "ubuntu/bionic64"
      node.vm.hostname = "client#{i}"
      node.vm.network "private_network", ip: "192.168.10.1#{i}", hostname: true

      # Install NFS on client
      node.vm.provision "InstallClientNFS", type: "shell", run: "once", inline: $installNFSClient

      # Mount NFS Folder after reboot every time
      # Also you can add following line at /etc/fstab but not recommended.
      # 192.168.10.2:/mnt/mirror    /mnt/mirror   nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
      node.vm.provision "MountNFS", type: "shell", run: "always", inline: "mount 192.168.10.2:/mnt/mirror /mnt/mirror"

      # Add temporary private and public key to server
      # CAUTION: The keys should be removed after initial configuration
      node.vm.provision "CopySSHKeys", type: "file", source: "ssh_keys/id_rsa.pub", destination: "/home/vagrant/"
      node.vm.provision "ConfigSSH", type: "shell", inline: <<-SCRIPT
      cat id_rsa.pub >> .ssh/authorized_keys
      SCRIPT

      # Copy files into client
      node.vm.provision "CopyClientPy", type: "file", source: "socket_test/client.py", destination: "/home/vagrant/", run: "always"

      # Install MPICH
      node.vm.provision "InstallMPICH", type: "shell", run: "once", inline: $installMPICH

    end

  end

end
