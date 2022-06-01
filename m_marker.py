import os
import importlib

class Marker:
    
    def process(self,prob_path,prob_rpt):
        
        module='.'.join(prob_path[2:-3].split(os.path.sep))
        prob_mod = importlib.import_module(module)
        prob_id=prob_rpt.get_id()
        
        prob_score=0
        
        if prob_id==1:
            prob_score+=0.5 if isinstance(prob_mod.a,float) else 0
            prob_score+=0.5 if prob_mod.b[1]=='7' else 0
            prob_score+=0.5 if prob_mod.c=="Hello, World!" else 0
            prob_score+=0.5 if prob_mod.d(24,7)==24*7 else 0
            prob_score+=0.5 if prob_mod.e.get_name() == "Hello, World!" else 0
            prob_score+=0.5 if prob_mod.f["name"]=="Hello, World!" and prob_mod.f["score"]==10 else 0
        
        prob_rpt.update_score(prob_score)