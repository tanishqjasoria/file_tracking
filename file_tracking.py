import hashlib
import numpy as np
import tarfile


def get_common_files(metadata_before, metadata_after):
  """Return the names of common files in both 'before' and 'after' metadata."""
  return list(set(metadata_before) - \
     (set(metadata_before) - set(metadata_after)))


def track_added(metadata_before, metadata_after):
  """Return the names of the files which have been added."""
  added = []
  files_before = list(metadata_before.keys())
  files_after = list(metadata_after.keys())
  for file_name in files_after:
    # Added files would not be present in the 'before' metadata.
    if file_name not in files_before:
      added.append(file_name)
  return added


def track_removed(metadata_before, metadata_after):
  """Return the name of the files which have been removed."""
  removed = []
  files_before = list(metadata_before.keys())
  files_after = list(metadata_after.keys())
  for file_name in files_before:
    # Removed files would not be present in the 'after' metadata.
    if file_name not in files_after:
      removed.append(file_name)
  return removed


def track_unchanged(metadata_before, metadata_after):
  """Return the name of the files which are unchanged."""
  unchanged = []
  # Unchanged files must be common in both the metadata.
  common_files = get_common_files(metadata_before, metadata_after)
  for file_name in common_files:
    # Extracting the files with same hash.
    if metadata_before[file_name] == \
        metadata_after[file_name]:
      unchanged.append(file_name)
  return unchanged


def track_modified(metadata_before, metadata_after):
  """Return the name of the files which are modified."""
  modified = []
  # Modified files must be common in both the metadata.
  common_files = get_common_files(metadata_before, metadata_after)   
  for file_name in common_files:
    # Extracting the files with different hash.
    if metadata_before[file_name] != \
        metadata_after[file_name]:
      modified.append(file_name)
  return modified


def track(metadata_before, metadata_after):
  """Track the changes using 'before' and 'after' metadata."""
  added = track_added(metadata_before, metadata_after)
  modified = track_modified(metadata_before, metadata_after)
  unchanged = track_unchanged(metadata_before, metadata_after)
  removed = track_removed(metadata_before, metadata_after)
  return added, modified, unchanged, removed


def calculate_hash(fileobj):
  """Calculate SHA1 hash of a file."""
  BLOCKSIZE = 65536  
  hasher = hashlib.sha1()
  # Break the file in small parts and then hash, helps in handeling large files.
  buff = fileobj.read(BLOCKSIZE)  
  while len(buff) > 0:  # Is data still left?  
    hasher.update(buff)  # Add data block to the hasher.
    buff = fileobj.read(BLOCKSIZE)
  return hasher.hexdigest()


def calculate_metadata(tarfilename):
  """Calculate metadata from a tar.gz file."""
  metadata = dict()
  # Open tarfile with tranparent compression to avoid different
  # hash genration due to different types of compression used.
  tarfileobj = tarfile.open(tarfilename,'r:*')  
  for member in tarfileobj.getnames():
    memberobj=tarfileobj.extractfile(member)
    if memberobj is not None:  # Is it a file or a folder?
        SHA1 = calculate_hash(memberobj)
        metadata.update({member:SHA1})
  tarfileobj.close()
  return metadata


def main():
  print("Select 0 or 1:")
  print("0) Do you want to use 'before' and 'after' metadata to track changes?")
  print("1) Do you want to use 'before' and 'after' tar.gz file to track changes?")
  userinput = int(input().strip())
  # Extract metadata according to the users choice.
  if userinput == 1:
    tarfilename_before = "zip_before.tar.gz"
    tarfilename_after = "zip_after.tar.gz"
    metadata_before = calculate_metadata(tarfilename_before)
    metadata_after = calculate_metadata(tarfilename_after)
  elif userinput == 0:
    metadata_before = np.load('metadata_before.npy').item()
    metadata_after = np.load('metadata_after.npy').item()
  else:
    print("'" + userinput + "' is not a valid input!")
  
  added, modified, unchanged, removed = track(metadata_before, metadata_after)
  
  print("added =", end = " ")
  print(added)
  print("modified =", end = " ")  
  print(modified)
  print("unchanged =", end = " ") 
  print(unchanged)
  print("removed =", end = " ") 
  print(removed)





if __name__ == '__main__':
  main()