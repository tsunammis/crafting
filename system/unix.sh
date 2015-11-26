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
