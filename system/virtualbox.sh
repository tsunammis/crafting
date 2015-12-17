# Host only
VBoxManage list hostonlyifs

# Delete hostonly by name
VBoxManage hostonlyif remove vboxnet0

# Mount share folder between host (ex: macosx) and client (ex: ubuntu)
sudo mount -t vboxsf workspace /workspace
