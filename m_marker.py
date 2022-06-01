import os
import importlib

class Marker:
    
    def process(self,prob_path,prob_rpt):
        
        module='.'.join(prob_path[2:-3].split(os.path.sep))
        prob_mod = importlib.import_module(module)
        prob_id=prob_rpt.get_id()
        
        prob_score=0
        
        prob_rpt.update_score(prob_score)