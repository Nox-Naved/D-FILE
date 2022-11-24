import os
from platform import architecture
if architecture()[0]=='64bit':os.system('git pull;chmod +x dfile;./dfile')
else:os.system('git pull;chmod +x dfile32;./dfile32')
