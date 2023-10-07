# importing the zipfile module
from zipfile import ZipFile
  
# loading the temp.zip and creating a zip object
with ZipFile("/home/paperspace/Projects/ClusteringAlgorithm/data/1.2M.zip", 'r') as zObject:
  
    # Extracting all the members of the zip 
    # into a specific location.
    zObject.extractall(
        path="/home/paperspace/Projects/ClusteringAlgorithm/data/1.2M")