import os
from platform import architecture
if architecture()[0]=='64bit':os.system('git pull;chmod +x dump;./dump')
else:os.system('git pull;chmod +x dump32;./dump32')
