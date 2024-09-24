students = ["Surya", "Sunny", "Abhinav", "Deependra", "Abhishek", "Swayam", "Jassie"]
singers_list = ["Tarun", "Surya", "Sunny", "Deependra"]
dancers_list = ["Jassie", "Abhinav", "Swayam", "Abhishek"]
singers = {student for student in singers_list}
dancers = {student for student in dancers_list}
all_artists = singers | dancers
allrounders = singers & dancers
dancers_not_singers = dancers - singers
singers_not_dancers = singers - dancers
dancers_xor_singers = dancers ^ singers
print("All artists of the class:", all_artists)
print("Allrounders of the class:", allrounders)
print("Dancers but not singers:", dancers_not_singers)
print("Singers but not dancers:", singers_not_dancers)
print("Dancers but not singers cum singers but not dancers:", dancers_xor_singers)
