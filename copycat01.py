#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Pushing files around using shutil and os from the standard library"""

   def main():
    """code to move files around"""

# imports libr that are not common but needed for interacting with the OS and filesystem
import shutil
import os

# calls the os libr function to change our directory to ensure we start in the correct path
os.chdir("/home/student/mycode/")

# calls the shell utility functions to copy (A) a single file and (B) a directorty and all its files

# (A)
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# (B)
shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
