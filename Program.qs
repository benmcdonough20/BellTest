//this program shows that with two entangled qubits in boxed A and B separated by arbitrary distance, even though
//faster-the-light transmission is dissallowed, a statistically improbable correlation can be shown when measurements 
//are taken in known bases and compared.

namespace Program {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    //A measurements: Z = \0>, \1>  X = |+>, |->
    //B measurements: W = 1/sqrt(2)[Z+X], V = 1/sqrt(2)[Z-X]

    //try to visualize these as projection axis on the bloch sphere

    operation ZW() : (Result, Result) { //Z refers to the basis on the first qubit, W the basis of the second
        using(register = Qubit[2]){
            //first prepare the system in an entangled state of 1/sqrt(2)[|00>+\11>]
            H(register[0]);
            CNOT(register[0], register[1]); //conditioned X gate set system in entanglement
            //prepare the measurement bases
            S(register[1]); //most standard operators can be formed from the phase shift T and Hadamard gates
            H(register[1]);
            T(register[1]);
            H(register[1]);
            //note the deffered measurement, it doesn't matter when the system in measured, and applying the SHTH then measuring in the Z basis is equivalent to the W basis
            let state = (M(register[0]), M(register[1]));
            ResetAll(register);
            return state;
        }
    } 

    operation ZV() : (Result, Result) {
        using( register = Qubit[2]){
            H(register[0]);
            CNOT(register[0], register[1]);
            //prepare measurement bases
            S(register[1]);
            H(register[1]);
            Adjoint T(register[1]);
            H(register[1]);
            
            let state = (M(register[0]), M(register[1]));
            ResetAll(register);
            return state;
        }
    }

    operation XW() : (Result, Result) {
        using( register = Qubit[2]){
            H(register[0]);
            CNOT(register[0], register[1]);
            //prepare bases
            H(register[0]);

            S(register[1]);
            H(register[1]);
            T(register[1]);
            H(register[1]);

            let state = (M(register[0]), M(register[1]));
            ResetAll(register);
            return state;
        }
    }

    operation XV() : (Result, Result) {
        using(register = Qubit[2]){
            H(register[0]);
            CNOT(register[0], register[1]);
            //prepare bases

            H(register[0]);

            S(register[1]);
            H(register[1]);
            Adjoint T(register[1]);
            H(register[1]);
            
            let state = (M(register[0]), M(register[1]));
            ResetAll(register);
            return state;
        }
    }
}