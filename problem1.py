# Tasks:
# Compute each student's average
# Find the top-performing student
# Add a "status" field:
# "Pass" if average ≥ 75
# "Fail" otherwise
# Sort students by average (descending)
# 💡 Concepts: lists, dictionaries, sorting, lambda

Linda = {"History" : 87,
         "English" : 92,
         "Math" : 89,
         "Chemistry" : 90,
         "Physics" : 92
         }

Ace = {"History" : 89,
         "English" : 93,
         "Math" : 90,
         "Chemistry" : 87,
         "Physics" : 90
         }

Gabriel = {"History" : 92,
         "English" : 91,
         "Math" : 87,
         "Chemistry" : 82,
         "Physics" : 93
         }

lindaSubjectNum = 0
lindaGradeSum = 0
for i in Linda:
    print(f"Linda's grade in {i} is {Linda[i]}")
    lindaGradeSum += Linda[i]
    lindaSubjectNum += 1

lindaAvg = lindaGradeSum/lindaSubjectNum
print(f"\nLinda's average is {lindaAvg}\n")

AceSubjectNum = 0 
aceGradeSum = 0
for i in Ace:
    print(f"Ace's grade in {i} is {Ace[i]}")
    aceGradeSum += Ace[i]
    AceSubjectNum += 1

aceAvg = aceGradeSum/AceSubjectNum
print(f"\nAce's average is {aceAvg}\n")

gabrielSubjectNum = 0 
gabrielGradeSum = 0
for i in Ace:
    print(f"Gabriel's grade in {i} is {Gabriel[i]}")
    gabrielGradeSum += Gabriel[i]
    gabrielSubjectNum += 1

gabrielAvg = gabrielGradeSum/gabrielSubjectNum
print(f"\nAce's average is {gabrielAvg}")