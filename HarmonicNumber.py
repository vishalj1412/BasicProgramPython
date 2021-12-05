
# Function to find N-th Harmonic Number
def nthHarmonic(N) :
 
    harmonic = 1.00
 
    for i in range(2, N + 1) :
        harmonic += 1 / i
 
    return harmonic
     
if __name__ == "__main__" :
 
    N = int(input("enter value of N : "))
    print(round(nthHarmonic(N),5))
 