# Intervals
WT = 2
HT = 1
#
List_of_all_Notes = ["C", "C#","D","D#","E","F","F#","G","G#","A","A#","B"]
Major_scale = [WT, WT, HT, WT, WT, WT, HT]
Minor_scale = [WT, HT, WT, WT, HT, WT, WT]
Harmonic_Minor_scale = [WT, HT, WT, WT, HT, WT+HT, HT]


Scale_Types = [Major_scale, Minor_scale, Harmonic_Minor_scale]
# print("\n All notes in Music are:")
# print(List_of_all_Notes)

# ----------------------------Basic---------------------------------------
#A function to check if the note lies in the scale
def Search_note_in_scale(Note, Scale):
    Note_found = False
    for note in range(len(Scale)):
        # print("Comparing", Note, "with", Scale[note])
        if Scale[note] == Note:
            return True
    return False

#A function to get the position of note in the list
def Find_Index_in_list(Note):
   return List_of_all_Notes.index(Note)

#A function to access the list cyclically
def Calc_new_Index(Index, Interval):
    new_index = Index + Interval
    if new_index >=12:
        new_index = new_index -12
    return new_index
   
#A function to find the note in given interval
def Find_note_using_Interval(Note, Interval):
    index = Find_Index_in_list(Note)
    new_index = Calc_new_Index(index, Interval)
    return List_of_all_Notes[new_index]

#A function that calculates the scale based on Interval formulas
def Calc_Scale(Note, Formula):
    key_index = Find_Index_in_list(Note)
    Calculated_Scale = [Note]
    for iterator in range(7):
        next_note = Find_note_using_Interval(Note, Formula[iterator])
        # Store in a list
        Calculated_Scale.append(next_note)
        Note = next_note
    return Calculated_Scale


# ----------------------------Basic---------------------------------------

# Key = input("Enter the key:")
# Calc_Scale("A", Minor_scale)

# --------------------------User Input----------------------------------
# Multiple input from the user
entered_Notes = [str(Entered_Notes) for Entered_Notes in input("Enter multiple Notes: ").split()]
# print(Entered_Notes)
# ------------------------Provide scales---------------------------------
def Calc_possible_scales(Entered_Notes):
    counter = 0
    Scale_Found = False
    for scale_type in range(len(Scale_Types)):
        for scale in range(len(List_of_all_Notes)):
            Searched_scale = Calc_Scale(List_of_all_Notes[scale], Scale_Types[scale_type])
            Note_Found = False
            counter = 0
            for value in range(len(Entered_Notes)):
                Note_Found = Search_note_in_scale(Entered_Notes[value],         Searched_scale)
                if(Note_Found == True):
                    counter = counter +1
                if(counter == len(Entered_Notes)):
                    print("Notes belong to", Searched_scale[0], scale_type)
                    Scale_Found = Scale_Found +1
               
    if(Scale_Found == 0):
        print("Notes do not belong to a major scale")
 
Calc_possible_scales(entered_Notes)
