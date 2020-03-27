def addition(n1:int, n2:int)-> int:
    
    if type(n1) != int and type(n2) != int:
        raise TypeError
        
    return n1+n2
    
    
def sub(n1:int, n2:int)-> int:
    
    if type(n1) != int and type(n2) != int:
        raise TypeError
        
    return n1-n2
    