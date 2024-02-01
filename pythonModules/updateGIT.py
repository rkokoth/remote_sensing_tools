import os
import argparse

'''
This code automates the git-venrsion  control process.
'''

parser = argparse.ArgumentParser()
parser.add_argument("remote_branch", help="repository is the name of the remote branch you want to commit the changes to.")
parser.add_argument("dir", help="dir is the path to the folder where files that are tracked are located.")
args = parser.parse_args()
print(args.remote_branch)
print(args.dir)
checkout_command = 'git chechout xxx'
add_commad = ''
commit_commad = ''
push_commad = ''






