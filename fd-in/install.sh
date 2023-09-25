#!/bin/bash

# Ask the user to enter the device (e.g., /dev/sdb)
read -p "Enter the device (e.g., /dev/sdb): " device

# Check if the device exists
if [ ! -e "$device" ]; then
    echo "Device not found: $device"
    exit 1
fi

# List partitions on the specified device
sudo fdisk -l $device

# Ask for confirmation to format the device
read -p "Proceed with formatting? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 0
fi

# Ask the user for the directory name
read -p "Enter the directory name: " dir_name

# Create LUKS encrypted volume
sudo cryptsetup --verbose --verify-passphrase luksFormat "$device"2
read -p "Enter 'YES' to confirm: " confirmation
if [ "$confirmation" != "YES" ]; then
    echo "Aborted."
    exit 0
fi

# Open LUKS volume
sudo cryptsetup luksOpen "$device"2 "$dir_name"

# Create an ext3 filesystem
sudo mkfs.ext3 /dev/mapper/"$dir_name"

# Label the filesystem
sudo e2label /dev/mapper/"$dir_name" persistence

# Create a mount point
sudo mkdir -p /mnt/"$dir_name"

# Mount the filesystem
sudo mount /dev/mapper/"$dir_name" /mnt/"$dir_name"

# Create persistence.conf
echo "/ union" | sudo tee /mnt/"$dir_name"/persistence.conf > /dev/null

# Unmount the filesystem
sudo umount /mnt/"$dir_name"

# Close the LUKS volume
sudo cryptsetup luksClose /dev/mapper/"$dir_name"

echo "Setup completed successfully."
