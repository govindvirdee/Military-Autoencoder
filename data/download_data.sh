#!/bin/bash

# Script to download the NSL-KDD dataset

DATASET_URL="http://205.174.165.80/CICDataset/NSL-KDD/"

# Directory to store the downloaded dataset
DATA_DIR="./raw"

# Create the data directory if it doesn't exist
if [ ! -d "$DATA_DIR" ]; then
  echo "Creating data directory: $DATA_DIR"
  mkdir -p $DATA_DIR
fi

# Downloading the dataset
echo "Downloading NSL-KDD dataset..."
curl -L $DATASET_URL -o $DATA_DIR/archive.zip

# Unzip the dataset if it's zipped
echo "Unzipping the dataset..."
unzip -o $DATA_DIR/archive.zip -d $DATA_DIR

echo "Dataset download and extraction complete."
