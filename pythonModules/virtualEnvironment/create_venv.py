import os
import sys
args = sys.argv
def recreate_environment(venname = args[1]):
    if not os.path.isdir(os.path.join(os.getcwd(), venname)):
        os.system(f'python3 -m venv {os.path.join(os.getcwd(), venname)}')
        print(f'created  {venname} successfully')

recreate_environment()