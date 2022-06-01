from m_env import *

class ProblemReport:
    _stt=None
    _score=0
    
    def __init__(self,ind) -> None:
        self._id=ind
    
    def update_stt(self,stt):
        self._stt=stt 

    def update_score(self,score):
        self._score=score
    
    def get_id(self):
        return self._id
        
    def get_score(self):
        return self._score
    
    def get_stt(self):
        return self._stt

class Report:
    # NOTE
    # With "_probs=[]", all "Report" objects's "_probs" will point to the same memory location. 
    def __init__(self,ind) -> None:
        self._probs=[] 
        self._id=ind
        
    def get_id(self):
        return self._id
    
    def get_probs(self):
        return self._probs
    
    def get_score(self):
        return sum([prob.get_score() for prob in self._probs if prob.get_stt()==SUCCESS])
   
    def add_prob(self,prob):
        self._probs.append(prob)
        