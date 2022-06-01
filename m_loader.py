import os
import glob

from m_env import BASE_HOME,SM_DIR 

class Loader:
    def process(self):
        sm_root=os.path.join(BASE_HOME,SM_DIR)
        sm_home_list=glob.glob(os.path.join(sm_root,"*"))
        return sm_home_list

