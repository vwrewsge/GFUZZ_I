x�M�A�@������4Ͳ��%)�߳=T�f���]���WH��h:$�dX�A��!T���.� .�(��{ΫS�݊t��:��+�l9��M��D�P~qjg�ku��@F�v
��  A�

import zlib
import os

decompressed_data = zlib.decompress(compressed_data)

# Specify the path to save the decompressed file
output_path = "./tmp/decompressed_file.txt"

# Save the decompressed data to a file
with open(output_path, "wb") as file:
    file.write(decompressed_data)

print("File extracted successfully to:", output_path)