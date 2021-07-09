"""
GROUP-3

>>DFA to accept the set of strings containing not more than 3 zeroes. 

Solution:

 L={λ,1,0,10,100,1000,110,101,000,00,0,....}
 L'={0000,10000,00011100,10101010....}

Transition Table:

-------Q-States-----------|-Σ-Alphabets-|-----
		                  |  0  |  1    |
--------------------------|-----|-------|-----
 (Start/Final)	A	      |  B  |  A    |
--------------------------|-----|-------|-----
 (Final)	    B         |  C  |  B    |
--------------------------|-----|-------|-----
 (Final)	    C         |	 D  |  C    |
--------------------------|-----|-------|-----
 (Final)	    D         |  T  |  D    |
--------------------------|-----|-------|-----
 (Trap)		    T         |  T  |  T    |
--------------------------|-----|-------|----

DFA:

 M=(Q,Σ,δ,q0,F)

 Q={A,B,C,D,T}
 Σ={0,1}
 δ={
   δ(A,0)=B
   δ(A,1)=A
   δ(B,0)=C
   δ(B,1)=B
   δ(C,0)=D
   δ(C,1)=C
   δ(D,0)=T
   δ(D,1)=D
   δ(T,0)=T
   δ(T,1)=T
  }

 q0=A
 F={A,B,C,D}

"""

#Program:

from re import search

final_state="A"
transition_diagram=""

#Start State A :takes the string s and the position i of the character to read
def A(s,i):
	
	global final_state
	global transition_diagram
	
	final_state="A"
	
	#Add the state to transition_diagram
	transition_diagram=transition_diagram+final_state+"->"
	
	#If string read is empty
	if len(s)==0:
		transition_diagram+="A"
		return
	
	#If reading the string is finished 	
	if i==len(s):
		transition_diagram=transition_diagram[:-2] #to remove "->"
		return
		
	#If the char read is '0' go to next state B	
	if s[i]=='0':
		i+=1
		B(s,i)
		
	#If the char read is '1' remain in state A
	else:
		i+=1
		A(s,i)

def B(s,i):
		
	global final_state
	global transition_diagram
	
	final_state="B"
	
	#Add the state to transition_diagram
	transition_diagram=transition_diagram+final_state+"->"
	
	#If reading the string is finished
	if i==len(s):
		transition_diagram=transition_diagram[:-2]
		return
		
	#If the char read is '0' go to next state C
	if s[i]=='0':
		i+=1
		C(s,i)
	
	#If the char read is '1' remain in state B
	else:
		i+=1
		B(s,i)
		
def C(s,i):
		
	global final_state
	global transition_diagram
	
	final_state="C"
	
	#Add the state to transition_diagram
	transition_diagram=transition_diagram+final_state+"->"
	
	#If reading the string is finished
	if i==len(s):
		transition_diagram=transition_diagram[:-2]
		return
		
	#If the char read is '0' go to next state D
	if s[i]=='0':
		i+=1
		D(s,i)
		
	#If the char read is '1' remain in state C
	else:
		i+=1
		C(s,i)
		
def D(s,i):
		
	global final_state
	global transition_diagram
	
	final_state="D"
	
	#Add the state to transition_diagram
	transition_diagram=transition_diagram+final_state+"->"
		
	#If reading the string is finished
	if i==len(s):
		transition_diagram=transition_diagram[:-2]
		return
		
	#If the char read is '0' go to next state T
	if s[i]=='0':
		i+=1
		T(s,i)
	
	#If the char read is '1' remain in  state D
	else:
		i+=1
		D(s,i)

#Trap State		
def T(s,i):
		
	global final_state
	global transition_diagram
	
	final_state="T"
	
	#Add the state to transition_diagram
	transition_diagram=transition_diagram+final_state+"->"
	
	#If reading the string is finished
	if i==len(s):
		transition_diagram=transition_diagram[:-2]
		return
		
	#If the char read is '0' remain in state T
	if s[i]=='0':
		i+=1
		T(s,i)
		
	#If the char read is '1' remain in  state T
	else:
		i+=1
		T(s,i)
		

#Main Namespace	
if __name__ == "__main__":

	print("\n\t>>DFA to accept the set of strings containing not more than 3 zeroes<<")
	print("-------------------------------------------------------------------------------------")
	
	#Input String
	inp=input(" Enter a string: ")

	#Check if input string contains other than 0 or 1
	if search("[a-zA-z2-9]",inp):
		print(" Invalid Input String❌")  
	
	else:
		
		#Start Transition by reading the character at 0th index(first char) of input string  
		A(inp,0)

		if final_state=="T":
			
			print(f" {inp} is Rejected❗")
			print(" --------------------")
			print(" Transition: ")
			print(" (Start)"+transition_diagram+"(Trap State)")
			print("\n")
		
		else:
		
			print(f" {inp} is Accepted ✔")
			print(" --------------------")
			print(" Transition: ")
			print(" (Start)"+transition_diagram+"(Final)")
			print("\n")
			
