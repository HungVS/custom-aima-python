import os
import glob
import shutil

from m_loader import Loader
from m_report import ProblemReport, Report
from m_marker import Marker 
from m_persister import Persister
from m_utils import isolate
from m_env import BASE_HOME,SM_DIR 
from pathlib import Path


def remove_cache():
    cache_dir="__pycache__"
    for cache_home in list(Path(os.path.join(BASE_HOME,SM_DIR)).rglob(cache_dir)):
        cache_home=cache_home.__str__()
        shutil.rmtree(cache_home)

def main():
    loader=Loader()
    marker=Marker()
    persister=Persister()

    for sm_home in loader.process():
        sm_id=os.path.basename(sm_home)
        sm_rpt=Report(sm_id)
        prob_path_list=glob.glob(os.path.join(sm_home,"*"))
        for prob_path in prob_path_list: 
            prob_id=int(os.path.basename(prob_path)[-4:-3])
            prob_rpt=ProblemReport(prob_id)
            sm_rpt.add_prob(prob_rpt)
            
            prob_stt=isolate(marker.process,prob_path,prob_rpt) 
            prob_rpt.update_stt(prob_stt)
            
        persister.process(sm_rpt)
        
remove_cache()
main() 