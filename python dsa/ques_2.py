coursecode = input("What is the coursecode?")
coursecode = [str(y) for y in coursecode.split(',')]
coursename = input("what is the coursename?")
coursename = [str(z) for z in coursename.split(',')]
course_details_zip = zip(coursecode,coursename)


rollnumber = input("What is the rollnumber?")
rollnumber = [str(p) for p in rollnumber.split(',')]
name = input("what is the name?")
name = [str(q) for q in name.split(',')]
student_details_zip = zip(rollnumber,name)


grade = input("what is the grade?")
grade = [str(r) for r in grade.split(',')]
grades_zip = zip(rollnumber,coursecode,grade)

print(list(course_details_zip))
print(list(student_details_zip))
print(list(grades_zip))
combo = zip((course_details_zip,student_details_zip,grades_zip))
print(list(combo))

# Test Case 4 	

#transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")],[("UGM2018001","MA101","AB"),("UGP2018132","PH101","B"),("UGM2018001","PH101","B")])

	

#[('UGM2018001', 'Rohit Grewal', [('MA101', 'Calculus', 'AB'), ('PH101', 'Mechanics', 'B')]), ('UGP2018132', 'Neha Talwar', [('PH101', 'Mechanics', 'B')])]

#Test Case 5 	

#transcript([("T1","Test 1"),("T2","Test 2"),("T3","Test 3")],[("Opener","Murali Vijay"),("Captain","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Opener","T1","14"),("Captain","T1","33"),("No3","T1","30"),("Opener","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Opener","T3","33"),("Captain","T3","95"),("No3","T3","51")])

	

#[('Captain', 'Virat Kohli', [('T1', 'Test 1', '33'), ('T2', 'Test 2', '158'), ('T3', 'Test 3', '95')]), ('No3', 'Cheteshwar Pujara', [('T1', 'Test 1', '30'), ('T2', 'Test 2', '19'), ('T3', 'Test 3', '51')]), ('Opener', 'Murali Vijay', [('T1', 'Test 1', '14'), ('T2', 'Test 2', '55'), ('T3', 'Test 3', '33')])]



#countries = ["Italy", "Germany", "Spain", "USA"]
#country_specialities_zip = zip(dishes,countries)
#print(list(country_specialities_zip))
#country_specialities_list = list(country_specialities_zip)
#country_specialities_dict = dict(country_specialities_list)
#print(country_specialities_dict)

# >>> knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
# >>> knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
# >>> knowledge.update(knowledge2)
# >>> knowledge
# {'Frank': {'Python', 'Perl'}, 'Guido': {'Python'}, 'Monica': {'C', 'C++'}}


