Question=(("Which molecule has a non-zero dipole moment?"),
          ("The hybridization of carbon atoms in benzene is:"),
          ("The oxidation state of cobalt in the complex [Co(NH₃)₆]Cl₃ is:"),
          ("Which of the following ligands is bidentate?"),
          ("The IUPAC name of the compound CH₃CH₂C≡CH is:"),("Which factor does NOT affect the rate of a chemical reaction?"),
          )
option=(("A. BF₃"," B. CO₂ ","C. H₂O"," D. CCl₄"),
        ("A. sp","B. sp²","C. sp³","D. dsp²"),
        ("A. +1","B. +2","C. +3","D. 0"),
        ("A. NH₃","B. H₂O","C. en (ethylenediamine)","D. Cl⁻"),
        ("A. But-1-yne","B. But-2-yne","C. 1-Butyne","D. Both A and C"))  
Choice=[]   
answer=("A","B","C","C","D")  
score=0
Question_num=0
for q in Question:
    print ("-----------------")
    print(q)
    for op in option[Question_num]:
        print(op)
    Choice=input("Enter the Answer :").upper()
    #Choice.append(op)
    if Choice==answer[Question_num]:
       
        score+=1
        print("---CORRECT----")
    else:
        print("---WRONG---")
        print(f"{answer[Question_num ] }is the correct")
        Question_num+=1
print("--------------------") 
print("------RESULT--------")
print("--------------------") 
print("Answer: ",end=" ")
for ans in answer:
    print(ans,end=" ")
print()
print("Guesses: ",end=" ")
for a in Choice:
    print(a,end=" ")
print()
score=int(score/len(Question)*100)
print(f"Your score is {score}%")
        