import matplotlib.pyplot as plt 

def check_transition(s1, s2):
    
    purines = {'A' , 'G'}
    pyrimidines = {'C' , 'T'}
    
    return (s1 in purines and s2 in purines) or (s1 in pyrimidines and s2 in pyrimidines)

def check_transversion(s1, s2):
    
    purines = {'A' , 'G'}
    pyrimidines= {'C', 'T'}
    
    return (s1 in purines and s2 in pyrimidines) or (s1 in pyrimidines and s2 in purines)

def count_transition_transversion(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("SEQUENCE MUST BE OF EQUAL SIZE")
    
    transitions=0 
    transversions=0
    
    for a, b in zip(s1,s2):
        
        if a == b:
            continue
        
        if check_transition(a,b):
            transitions+=1
            
        elif check_transversion(a,b):
            transversions+=1
        
        else:
            pass 
        
    print("Transitions:", transitions)
    print("Transversion:",transversions)
    
    return transitions, transversions

def transition_transversion_ratio(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("SEQUENCE MUST BE OF EQUAL SIZE")
    
    transitions=0
    transversions=0
    
    for a, b in zip(s1,s2):
        
        if a==b:
            continue
        
        if check_transition(a,b):
            transitions+=1
            
        elif check_transversion(a,b):
            transversions+=1
        
        else:
            pass 
    if transversions == 0:
        return float('inf')
    
    return transitions/ transversions 

     
s1 = input("Enter nucleotide of DNA1:").upper()
s2 = input("Enter nucleotide of DNA2:").upper()

ti, tv= count_transition_transversion(s1, s2)

print("Transition", ti)
print("Transversion", tv)

ti_tv_ratio= transition_transversion_ratio(s1, s2)
print("Transition and transversion ratio is" , ti_tv_ratio)

#PLOTTING 
categories = ['Transition', 'Transversion']
counts = [ti, tv]

plt.figure(figsize=(6,4))
plt.bar(categories, counts, color=['skyblue', 'salmon'])

plt.ylabel("Count")
plt.title("Transition and transversion count")

for i, v in enumerate(counts):
    plt.text(i, v + 0.1, str(v), ha='center', va='bottom')
plt.tight_layout()
plt.show()




