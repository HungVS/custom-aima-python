import os
import importlib
import inspect

from csp import NQueensCSP
from utils import Symbol, expr
from m_utils import is_true, log_noti

class Marker:
    
    def process(self,prob_path,prob_rpt):
        
        module='.'.join(prob_path[2:-3].split(os.path.sep))
        prob_mod = importlib.import_module(module)
        prob_id=prob_rpt.get_id()
        
        prob_score=0
        
        if prob_id==1:
            c_id="I - PYTHON CO BAN"
            try:
                res=isinstance(prob_mod.a,float)
                prob_score+=0.75 if is_true(res) else 0
            except:
                log_noti(c_id, 'a')
            try:
                res=prob_mod.b[1]=='7' 
                prob_score+=0.75 if is_true(res)else 0
            except:
                log_noti(c_id, 'b')
            try:
                res=prob_mod.c=="Hello, World!" 
                prob_score+=0.75 if is_true(res)else 0
            except:
                log_noti(c_id, 'c')
            try:
                res=prob_mod.d(24,7)==24*7
                prob_score+=0.75 if is_true(res)else 0
            except:
                log_noti(c_id, 'd')
            try:
                res=prob_mod.e.get_name() == "Hello, World!"
                prob_score+=0.75 if is_true(res)else 0
            except:
                log_noti(c_id, 'e')
            try: 
                res=prob_mod.f["name"]=="Hello, World!"  and prob_mod.f["score"]==10
                prob_score+=0.75 if is_true(res) else 0
            except:
                log_noti(c_id, 'f')
            try:
                res=prob_mod.g(["Hello, ", "World", "!"])=="Hello, World!"
                prob_score+=0.75 if is_true(res) else 0
            except:
                log_noti(c_id, 'g')
            try:
                H=prob_mod.H
                h=H(10, "...", 22)
                res=h.get_infor()==[h._id,h._name,h._age]
                prob_score+=0.75 if is_true(res)else 0
            except:
                log_noti(c_id, 'h')
        
        elif prob_id==2:
            c_id="PHAN II - AI CO BAN"
            program=prob_mod.program
            try:
                res=program("green") == "go" and program("red") == "stop" and program("yellow") == "processing"
                prob_score+=0.25 if  is_true(res)else 0
            except:
                log_noti(c_id, 'a')
            try:
                res=prob_mod.node.state=="Hanoi"
                prob_score+=0.25 if is_true(res) else 0
            except:
                log_noti(c_id, 'b')
            try:
                res=round(prob_mod.sld((11.1,12.2),(24.7,30.2)))==23
                prob_score+=0.25 if is_true(res)else 0
            except:
                log_noti(c_id, 'c')
            try:
                res=round(prob_mod.T)==18 
                prob_score+=0.25 if is_true(res)else 0
            except:
                log_noti(c_id, 'd')
            try:
                sd=prob_mod.sd
                res=sd['A1']==list(range(1,10))
                prob_score+=0.25 if is_true(res)else 0 
            except:
                log_noti(c_id, 'e')
            try:
                csp=prob_mod.csp
                res=sorted(csp.variables)==['Hanam', 'Hanoi', 'Hungyen'] and csp.domains["..."]== ['R', 'G', 'B']
                prob_score+=0.25 if is_true(res)else 0
            except:
                log_noti(c_id, 'f')
            try: 
                s=prob_mod.s 
                res=s.op=='==>' and s.args[1]==Symbol('C')
                prob_score+=0.25 if is_true(res) else 0
            except:
                log_noti(c_id, 'g')   
            try:
                h=prob_mod.h
                s=expr("A==>B")
                op,args=h(s)
                res=op==s.op and args==s.args
                prob_score+=0.25 if is_true(res)else 0
            except:
                log_noti(c_id,'h')
            
        elif prob_id==3:
            try:
                distances=prob_mod.distances
                prob_score+=0.5 if sorted(prob_mod.all_cities)==['Bacgiang', 'Dienbien', 'Hanoi', 'LaoCai', 'Namdinh', 'Nghean'] else 0
                prob_score+=0.5 if round(distances["Hanoi"]["Dienbien"])==round(161.55494421403512) and round(distances["Namdinh"]["Bacgiang"])==round(130.38404810405297) else 0
            except AttributeError: 
                print(f"[CANH BAO]: KHONG DUOC DOI TEN CAC 'BIEN CO SAN'")
            src=inspect.getsource(prob_mod)
            if src.count("TSP_problem") == 1 or src.replace(" ", "").count("(50,250)")==1 or src.replace(" ", "").count("(320,280)")==1:
                print(f"[CANH BAO]: PHAT HIEN 'GIAN LAN', DA THUC HIEN 'DANH DAU BAI' TU DONG.\nCAN TU GIAC THONG BAO TA DE DUOC 'KHOAN HONG'")
                prob_score=0
            
        elif prob_id==4:
            initial=prob_mod.initial
            min_conflicts=prob_mod.min_conflicts
            eight_queens=prob_mod.eight_queens 
            
            prob_score+=0.5 if sorted(initial.values())==[0, 1, 2, 2, 3, 4, 5, 6] else 0
           
            ts_score=0 
            sol=min_conflicts(eight_queens,initial)
            
            ts_score+=1 if len(eight_queens.conflicted_vars(sol))==0 else 0
            
            src=inspect.getsource(min_conflicts)
            ts_score+=1 if src.count("min_conflicts_value") == 1 else 0
                
            # re_sol=None
            # for i in range(10):
            #     eight_queens=NQueensCSP(8)
            #     re_sol=min_conflicts(eight_queens,initial)
           
            # ts_score+= re_sol!=sol 
            
            prob_score+=0.5 if ts_score==2 else 0
            
        prob_rpt.update_score(prob_score)