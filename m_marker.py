import os
import importlib

from utils import Symbol

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
        
        elif prob_id==2:
            program=prob_mod.program
            prob_score+=0.5 if program("green") == "go" and program("red") == "stop" and program("yellow") == "processing" else 0
            prob_score+=0.5 if prob_mod.node.state=="Hanoi" else 0
            prob_score+=0.5 if round(prob_mod.sld((11.1,12.2),(24.7,30.2)))==23 else 0
            prob_score+=0.5 if round(prob_mod.T)==18 else 0
            csp=prob_mod.csp
            prob_score+=0.5 if sorted(csp.variables)==['Hanam', 'Hanoi', 'Hungyen'] and csp.domains["..."]== ['R', 'G', 'B'] else 0
            sd=prob_mod.sd
            prob_score+=0.5 if sd['A1']==list(range(1,10)) else 0 
            s=prob_mod.s 
            prob_score+=0.5 if s.op=='==>' and s.args[1]==Symbol('C') else 0
            
        prob_rpt.update_score(prob_score)