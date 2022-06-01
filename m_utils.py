import logging
from m_env import SUCCESS, ERROR

def match(inp, out):
    if inp==out:
        return 1
    return 0 

def match_batch(inps,outs):
    num_pairs=len(inps)
    pair_score=1 if num_pairs==sum([match(inps[i],outs[i]) for i in range(num_pairs)]) else 0
    return pair_score

# TODO x,y -> x
def isolate(f,x,y):
    try:
        f(x,y)
        return SUCCESS
    except ModuleNotFoundError:
        print("[ERROR]: Loi 'Module not found' - Can thong bao cho TA")
    except:
        logging.exception("Problem error")
        return ERROR

def match_dicts(d1,d2):
    if d1 == d2:
        return True
    else:
        return False
    
def log_noti(c_id, q_id):
    # print("================================================") 
    # logging.exception("")
    print(f"[CHU Y]: 'Chua' lam hoac lam 'sai' cau {q_id} - Phan {c_id}")
    # print("================================================") 