class Persister: 
    def process(self,sm_rpt):
        print(f"sm_id: {sm_rpt.get_id()} - score: {sm_rpt.get_score()}")  