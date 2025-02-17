import kagglehub

# Download data version
path = kagglehub.dataset_download("ander289386/cars-germany")

print("Path to dataset files:", path)
path = kagglehub.dataset_download("mexwell/electric-vehicle-charging-in-germany")

print("Path to dataset files:", path)

# So this code is downloading the dataset from kaggle
# and storing it in the kagglehub cashe directory
# I tried to direct the download to here
# but it doesn't work. there's an open issue on kagglehub repo abt this
# maybe I can run a script to move the files from the kagglehub cache to here
# but that's too much work for now, so I'll just manually relocate the files
# please note that running this script will not directly download the files to this directory