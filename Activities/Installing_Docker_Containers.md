# Activity: Installing Docker Containers for RHEL 9.4

## Step 1: Update the System
```bash
sudo dnf update
```

## Step 2: Install Docker
```bash
sudo dnf install docker
```

## Step 3: Start Docker Service
```bash
sudo systemctl start docker
```
**Error:** Failed to start `docker.service`: Unit `docker.service` not found.

## Step 4: Remove Docker (if necessary)
```bash
sudo dnf remove docker
```
**Note:** Installation failed using `dnf`, so I will attempt the installation using `yum`.

## Reference
For detailed installation instructions, visit the [Docker installation guide for RHEL](https://docs.docker.com/engine/install/rhel/).

## Step 5: Remove Existing Docker Packages
```bash
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine \
                  podman \
                  runc
```

## Step 6: Install YUM Utilities
```bash
sudo yum install -y yum-utils
```

## Step 7: Add Docker Repository
```bash
sudo yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
```

## Step 8: Install Docker Engine and Related Packages
```bash
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Step 9: Start Docker Service Again
```bash
sudo systemctl start docker
```

## Step 10: Add User to Docker Group
```bash
sudo usermod -aG docker u-user
```
**Note:** After adding the user to the Docker group, you need to log out of the system and log back in for the changes to take effect.

## Verification Commands
To verify that the Docker group was created, run the following command:
```bash
id
```
To check the Docker version, run:
```bash
docker version
```
<img width="1177" alt="Screenshot 2024-10-24 at 7 05 20 PM" src="https://github.com/user-attachments/assets/1d912d6d-f077-4a16-8e68-31941d527412">



