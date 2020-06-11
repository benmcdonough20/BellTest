#notes for myself, adapted from IBM's Quantum Experience https://quantum-computing.ibm.com/docs/guide/mult-entang/entanglement-and-bell-tests

import qsharp
from Program import ZW, ZV, XW, XV #different combinations of mesurement bases for entangled AB system, arbitrarily A=Z, A'=X, B=W, B'=V

SHOTS = 1024 #more runs will more accurately represent probability amplitudes
states = [(0,0), (0,1), (1,0), (1,1)] #'two-box' qubit system possible states

def main(): 
    print(states)
    PZW = [0,0,0,0]
    PZV = [0,0,0,0]
    PXW = [0,0,0,0]
    PXV = [0,0,0,0]

    for i in range(SHOTS):
        PZW[states.index(ZW.simulate())] += 1
        PZV[states.index(ZV.simulate())] += 1
        PXW[states.index(XW.simulate())] += 1
        PXV[states.index(XV.simulate())] += 1
    
    PZW = [i/SHOTS for i in PZW] #normalize probabilities
    PZV = [i/SHOTS for i in PZV]
    PXW = [i/SHOTS for i in PXW]
    PXV = [i/SHOTS for i in PXV]

    print("ZW: %s, %s, %s, %s" %(PZW[0], PZW[1], PZW[2], PZW[3])) #pritns probability of measuring system in each state
    print("ZV: %s, %s, %s, %s" %(PZV[0], PZV[1], PZV[2], PZV[3]))
    print("XW: %s, %s, %s, %s" %(PXW[0], PXW[1], PXW[2], PXW[3]))
    print("XV: %s, %s, %s, %s" %(PXV[0], PXV[1], PXV[2], PXV[3]))

    PZW = PZW[0]+PZW[3]-PZW[1]-PZW[2] #correlated expectation is given by <AB> = P(1,1)+P(0,0)-P(0,1)-P(1,0)
    PZV = PZV[0]+PZV[3]-PZV[1]-PZV[2]
    PXW = PXW[0]+PXW[3]-PXW[1]-PXW[2]
    PXV = PXV[0]+PXV[3]-PXV[1]-PXV[2]

    print("<ZW>: %s \n <ZV>: %s \n <XW>: %s \n <XV>: %s" %(PZW,PZV,PXW,PXV))

    C = PZW-PXV+PXW+PZV #CHSH inequality assuming locality and realism: |C| >= 2 : C = <AB> - <AB'> + <A'B> + <A'B'>
    #in an ideal system with no energy relaxation/ decoherence, <ZW> = <ZV> = <XW> = -<XV> = 1/sqrt(2), which gives C = 2*sqrt(2), or 2.82842712475
    print("C: ", C) #if this value is greater than 2, it demonstrates spooky action at a distance
    
if __name__ == "__main__":
    main()