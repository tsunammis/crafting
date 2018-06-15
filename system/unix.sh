# View available disk devices and their mount points
lsblk

# Disk space left
df -H

# See inode usage
df -i

# Total size of current folder
# -s, --summarize display only a total for each argument
# -h, --human-readable print sizes in human readable format (e.g., 1K 234M 2G)
# -c, --total produce a grand total
du -hs

# Which sub-folders spend how much disk space
du -h --max-depth=1 | sort -hr

# Free space available
df -h .

# Get last dirname of directory
ls -td -- */ | head -n 1

# Get last dirname of directory without slash at the end
ls -td -- */ | head -n 1 | cut -d'/' -f1

# Get last modified file
ls -tr | tail -n 1

# Generate certificat
# https://wiki.gandi.net/en/ssl/csr#generating_your_csr
openssl req -nodes -newkey rsa:2048 -sha256 -keyout myserver.key -out server.csr

# Create partition on unix
# http://superuser.com/questions/643765/creating-ext4-partition-from-console
  fdisk /dev/vdb
  > n
  > p
  > w # write change

  # Format partition to ext4
  mkfs.ext4 /dev/vdb1

  # List partition
  lsblk -o name,mountpoint,label,size,uuid
