total_chores = 4 
original_count =  total_chores
print(f"You have {original_count}chores to finish today!\n")

completed_count = 0 
chore_num = 1 

while chore_num <= total_chores:

    if chore_num == 1: next_chore = "Make your bed:"
    elif chore_num == 2: next_chore = "Feed the pet:"
    elif chore_num == 3: next_chore = "Take out the trash:"
    else: next_chore = "Wash the dishes:"

    answer = input(f"Have you finished: {next_chore}?(yes/no)")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore has been completed!")
    if answer == "no":
        completed_count -= 1
        chore_num -= 1
        print("Okay, finish it and check again.")

    print("Chores remaining:", total_chores - completed_count)
    print()

    print("-----All chores have been completed----")
    print("Great work today finishing all the chores finished for today!!!")

    # Now lets use our skills and write an infinite loop
    print("\n===== CHORE CHECKLIST SUMMARY====")
    print("Chores Assigned Today:", original_count)
    print("Chores Completed:", completed_count)
    print("Chores Remaining:", total_chores - completed_count)
    print("===============================================================================")