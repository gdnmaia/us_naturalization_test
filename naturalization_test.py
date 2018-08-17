#### G D. Maia - 2018 - Designing and Debugging ####

import fuzzywuzzy
from fuzzywuzzy import fuzz
import random

#### Quizz data, questions and answers ####
dict_quizz1A = {"\n\n1. What is the supreme law of the land? >   " : "the Constitution",
				 "\n\n2. What does the Constitution do? >   " : "sets up the government",
				 "\n\n3. The idea of self-government is in the first three words of the Constitution? >   " : "We the People",
				 "\n\n4. What is an amendement? >   " : "a change or addition to the Constitution",
				 "\n\n5. What do we call the first ten amendments to the Constitution? >    " : "the Bill of Rights", 
				 "\n\n6. What is one right or freedom from the First Amendment? >    " : "speech, religion, assembly, press, petition the government",
				 "\n\n7. How many amendments does the Constitution have? >   " : "27",
				 "\n\n8. What did the Declaration of Independence do? >   " : "declared our independence from Great Britain",
				 "\n\n9. What are two rights in the Declaration of Independence? >   " : "life, liberty, and pursuit of hapiness",
				 "\n\n10. What is freedom of religion? >   " : "practice a religion or not to practice a religion.",
				 "\n\n11. What is the economy system in the United States? >   " : "capitalist economy",
				 "\n\n12. What is the rule of the law? >   " : "Everyone must follow the law"}
dict_quizz1B = {"\n\n13. Name one branch or part of the government? >   " : "Congress",
				 "\n\n14. What stops one branch of government from becoming too powerful? >   " : "checks and balances, separation of power",
				 "\n\n15. Who is in charge of the executive branch? >   " : "the President",
				 "\n\n16. Who makes federal laws? >   " : "Congress, US legislature",
				 "\n\n17. What are the two part of the US government? >    " : "the Senate and the House of Representatives", 
				 "\n\n18. How many US Senators are there? >    " : "100",
				 "\n\n19. We elect an US senator for how many years? >   " : "6",
				 "\n\n20. Who is one of your state's US Senators now? >   " : "Duckworth and Durbin",
				 "\n\n21. The House of Representatives has how many voting members? >   " : "435",
				 "\n\n22. We elect a US Representative for how many years? >   " : "2",
				 "\n\n23. Name your US representative? >   " : "Rodney Davis",
				 "\n\n24. Who does a US Senator represents? >   " : "all people of the state",
				 "\n\n25. Why do some states have more Representatives than others? >  " : "because of the state population",
				 "\n\n26. We elect a President for how many years? >  " : "4",
				 "\n\n27. In what month do we vote for President? >  " : "November",
				 "\n\n28. What is the name of the President of the United States? >  " : "Donald Trump",
				 "\n\n29. What is the name of the Vice Presidecdnt of the United States? >  " : "Mike Pence",
				 "\n\n30. If the President can no longer serve, who becomes the President? >  " : "the Vice President",
				 "\n\n31. If both the President and the Vice President can no longer serve, who becomes the President? >  " : "the Speaker of the House",
				 "\n\n32. Who is the Commander in Chief of the military? >  " : "the President",
				 "\n\n33. Who signs bills to become laws? >  " : "the President",
				 "\n\n34. Who vetos bills? >  " : "the President",
				 "\n\n35. What does the President's Cabinet do? >  " : "advises the President",
				 "\n\n36. What are two Cabinet-level positions? >  " : "Secretary of State, Secretary of Defense",
				 "\n\n37. What does the juditial branch do? >  " : "reviews laws, explains laws, resolves disputes, decided if a law goes agasint the Constitution",
				 "\n\n38. What is the highest court in the United States? >  " : "the Supreme Court",
				 "\n\n39. How many justices are on the Supreme Court? >  " : "9",
				 "\n\n40. Who is the Chief Justice of the United States? >  " : "John Roberts",
				 "\n\n41. Under our Constitution, some power belong to the federal government. What is one power of the federal government? >  " : "print money, declare war, create an army, make treaties",
				 "\n\n42. Under our Constitution, some powers belong to the states. What is one power of the states? >  " : "education, police, fire department, driver's license, zoning and land use",
				 "\n\n43. Who is the governor of your state now? >  " : "Bruce Rauner",
				 "\n\n44. What is the Capital of your state? >  " : "Springfield",
				 "\n\n45. What are the two major political parties in the United States? >  " : "Democractic and Republican",
				 "\n\n46. What is the political party of the president now? >  " : "Republican",
				 "\n\n47. What is the name of the Speaker of the House of Representatives now? >  " : "Paul Ryan"}
dict_quizz1C = {"\n\n48. There are four amendments to the Constitution about who can vote. Describe one of them? >   " : "Citizens 18 and older can vote",
				 "\n\n49. What is one responsibility that is only for United States citizens? >   " : "serve on a jury and vote in a federal election",
				 "\n\n50. Name one right only for United States citizens? >   " : "vote in a federal election, run for federal office",
				 "\n\n51. What are two rights of everyone living in the United States? >   " : "freedom of expression, freedom of speech, freedom of assembly, freedom to petition the government, freedom of religion, the right to bear arms",
				 "\n\n52. What do we show loyalty to when we say the Pledge of Allegiance? >    " : "the United States, the flag", 
				 "\n\n53. What is one promise you make when you become a United States citizen? >    " : "give up loyalty to other countries",
				 "\n\n54. How old do citizens have to be to vote for President? >   " : "18 and older",
				 "\n\n55. WWhat are 2 ways that Americans can participate in their democracy? >   " : "vote, join a political party, join a campaign, join a civic group, join a community group, give an elected offical your opinion on an issue",
				 "\n\n56. When is the last day you can send in federal income tax forms? >   " : "April 15",
				 "\n\n57. When must all men register for the Service? >   " : "At age 18 and 26"}
dict_quizz2A = {"\n\n58. What is one reason colonists came to America? >  " : "freedom, political, religious, economic, escape persecution",
				"\n\n59. Who lived in America before the Europeans arrived? >  " : "Native Americans",
				"\n\n60. What group of people was taken to America and sold as slaves? >  " : "Africans",
				"\n\n61. Why did the colonists fight the British? >  " : "high taxes, british army stayed in their houses, and they didn't have self-government", 
				"\n\n62. Who wrote the Declaration of Independence? >  " : "Thomas Jefferson",
				"\n\n63. When was the Declaration of Independence adopted? >  " : "July 4, 1776",
				"\n\n64. There are 13 original states. Name three. >  " : "New Hampshire, Massachusetts, Rhode Island, New York, New Jersey, Pennsylvania, Delaware, Maryland, Virginia, North Carolina, South Carolina, Georgia",
				"\n\n65. What happened at the Constitutional Convention? >  " : "The Constitution was written",
				"\n\n66. When was the Constitution written? >  " : "1787",
				"\n\n67. The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers. >  " : "James Madison, Alexander Hamilton, John Jay, Publius",
				"\n\n68. What is one thing Benjamin Franklin is famous for? >  " : "US diplomat, started first free libraries",
				"\n\n69. Who is the \"Father of Our Country\" >  " : "George Washington",
				"\n\n70. Who was the first President? >  " : "George Washington"}			
dict_quizz2B = {"\n\n71. What territory did the United States buy from France in 1803? >  " : "Louisiana",
				"\n\n72. Name one war fought by the United Stated in 1800s. >  " : "1812, Mexican-American War, Civil War, Spanish-American War",
				"\n\n73. Name the U.S. war between the North and the South. >  " : "the Civil War",
				"\n\n74. Name one problem that led to the Civil War. >  " : "slavery",
				"\n\n75. What was one important thing that Abraham Lincoln did? >  " : "freed the slaves",
				"\n\n76. What did the Emancipation Proclamation do? >  " : "freed the slaves",
				"\n\n77. What did Suzan B. Anthony do? >  " : "fought for women's rights"}				
dict_quizz2C = {"\n\n78. Name one war fought by the United States in the 1900s. >  " : "World War 1, World War 2, Korean War, Vietnam War, Gulf War",
				"\n\n79. Who was President during World War I? >  " : "Woodrow Wilson",
				"\n\n80. Who was the President during the Great Depression and World War II? >  " : "Franklin Roosevelt",
				"\n\n81. Who did the United States fight in the World War II? >  " : "Japan, Germany, and Italy",
				"\n\n82. Before he was President during, Eisenhower was a general. What war was he in? >  " : " World War II",
				"\n\n83. During the Cold War, what was the main concern of the United States? >  " : "Communism",
				"\n\n84. What movement tried to end racial discrimination? >  " : "civil rights movement",
				"\n\n85. What did Martin Luther King, Jr. do? >  " : "fought for civil rights",
				"\n\n86. What major event happened on September 11, 2001, in the United States? >  " : "Terrorist attack",
				"\n\n87. Name one American Indian tribe in the United States. >  " : "Cherokee, Apache, Sioux, Chippewa, Pueblo, Creek, ect"}
dict_quizz3A = {"\n\n88. Name of the two longest rivers in the United States. >  " : "Mississipi, Missouri",
				"\n\n89. What ocean is on the West Cost of the United States? >  " : "Pacific",
				"\n\n90. What ocean is on the East Cost of the United States? >  " : "Atlantic",
				"\n\n91. Name one US territory. >  " : "Puerto Rico, US Virgin Islands, American Samoa, Northern Mariana Islands",
				"\n\n92. Name one state that borders Canada. >  " : "Maine, New Hampshire, Vermont, New York, Pennsylvania, Ohio, Michigan, Minnesota, North Dakota, Montana, Idaho, Washington, Alaska",
				"\n\n93. Name one state that borders Mexico. >  " : "California, Arizona, New Mexico, Texas",
				"\n\n94. What is the capital of the United States? >  " : "Washington, D.C.",
				"\n\n95. Where is the Statue of Liberty?* >  " : "New York Harbor, Hudson River"}				
dict_quizz3B = {"\n\n96. Why does the flag have 13 stripes? >  " : "because of the 13 original colonies",
				"\n\n97. Why does the flag have 50 stars?* >  " : "because there is one star for each state",
				"\n\n98. What is the name of the national anthem? >  " : "The Spar-Spangled Banner"}				
dict_quizz3C = {"\n\n99. When do we celebrate Independence Day? >  " : "July 4",
				"\n\n100. Name two national U.S. holidays. >  " : "New Year's day, Martin Luther King, Veterans Day, Memorial Day, Independence Day, Thanksgiven, Christmans"}


#### Dictionaries added to a list in order to sequentially index the different dictionaries
list_of_dict = [dict_quizz1A, 
				dict_quizz1B, 
				dict_quizz1C, 
				dict_quizz2A, 
				dict_quizz2B, 
				dict_quizz2C, 
				dict_quizz3A, 
				dict_quizz3B, 
				dict_quizz3C]


### Storing both correct and incorrect answers as the quizz progresses ###
### Note that both are global variables as data is stored in each  function ###
correct_answers = []
wrong_answers = [] 

####################################################################
############# Function to choose topics and sub-topics #############
####################################################################

def start():
	choose_civics_topic()

def choose_civics_topic():
	"""
	This function takes the user to the 
	topics and subtopics of this quizz
	"""
	print("1 - CIVICS TEST")
	print("A: Principles of the American Democracy (questions 1 to 12)")
	print("B: Systems of Government (questions 13 to 47)")
	print("C: Rights and Responsilities (questions 48 to 57)\n")
	print("---------------------------------------------------------------------------------------------")
	
	print("2 - AMERICAN HISTORY")
	print("A: Colonial Period and Independence (questions 58 to 70)")
	print("B: 1800s (questions 71 to 77)")
	print("C: Recent American History and Other Important Historical Information (questions 78 to 87)\n")
	print("---------------------------------------------------------------------------------------------")
	
	print("3 - INTEGRATED CIVICS")
	print("A: Geography (questions 88 to 95)")
	print("B: Symbols (questions 96 to 98")
	print("C: Holidays (questions 99 to 100) \n")


	answer = int(input("What topic do you want to select? 1, 2, or 3?"))


	if answer == 1:
		print("1 - CIVICS TEST")
		print("A: Principles of the American Democracy (questions 1 to 12)")
		print("B: Systems of Government (questions 13 to 47)")
		print("C: Rights and Responsilities (questions 48 to 57)\n")
	
		answer1 = input("What subtopic do you want to select from the CIVIS TEST session? A, B, or C?")
	
		if answer1 == "A" or answer1 == "a":
			print("A: Principles of the American Democracy (questions 1 to 12)")
			CIVICS_TEST_principles_of_american_democracy()
		elif answer1 == "B" or answer1 == "b":
			print("B: Systems of Government (questions 13 to 47)")
			CIVICS_TEST_systems_of_government()
		elif answer1 == "C" or answer1 =="c":
			print("C: Rights and Responsilities (questions 48 to 57)")
			CIVICS_TEST_Rights_and_Responsilities()
		else:
			print("ERROR ::: please select a letter that exists")
	

	elif answer == 2:
		print("2 - AMERICAN HISTORY")
		print("A: Colonial Period and Independence (questions 58 to 70)")
		print("B: 1800s (questions 71 to 77)")
		print("C: Recent American History and Other Important Historical Information (questions 78 to 87)\n")
	
		answer2= input("What subtopic do you want to select from the AMERICAN HISTORY session? A, B, or C?")
	
		if answer2 == "A" or answer2 == "a":
			print("A: Colonial Period and Independence (questions 58 to 70)")
			AMERICAN_HISTORY_Colonial_Period_and_Independence()
		elif answer2 == "B" or answer2 == "b":
			print("B: 1800s (questions 71 to 77)")
			AMERICAN_HISTORY_1800s()
		elif answer2 == "C" or answer2 == "c":
			print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
			AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
		else:
			print("ERROR :::: please select a letter that exists")


	elif answer == 3:
		print("3 - INTEGRATED CIVICS")
		print("A: Geography (questions 88 to 95)")
		print("B: Symbols (questions 96 to 98)")
		print("C: Holidays (questions 99 to 100) \n")
	
		answer3= input("What subtopic do you want to select from the INTEGRATED CIVICS session? A, B, or C?")
	
		if answer3 == "A" or answer3 == "a":
			print("A: Geography (questions 88 to 95)")
			INTEGRATED_CIVICS_Geography()
		elif answer3 == "B" or answer3 == "b":
			print("B: Symbols (questions 96 to 98")
			INTEGRATED_CIVICS_Symbols()
		elif answer3 == "C" or answer3 == "c":
			print("C: Holidays (questions 99 to 100)")
			INTEGRATED_CIVICS_Holidays()
		else:
			print("ERROR :::: please select a letter that exists")
	
	else:
		print("Please look at the number options")

####################################################################
############## Randomize items inside dictionary  ##################
####################################################################
def shuffle(civics_topic):
	"""
	The input of the function will 
	be the dictionary of the question
	and answers. The output will
	be a random question with answer.
	Gui, me: This is a random sampling without replacement
	"""
	
	questions = []
	answers = []
	
	i = 0
	while i < len(civics_topic):
		current_selection = random.choice(list(civics_topic.keys()))
		if current_selection not in questions:
			questions.append(current_selection)
			answers.append(civics_topic[current_selection]) 
			i = i + 1
	return questions, answers
	
####################################################################
################### Run quizz questions ############################
####################################################################
def run_questions(dictionary_number):
	"""This function cycles items of our list 
	of dictionaries with quizz topics"""

	questions, answers = shuffle(dictionary_number)     #### Shuffling 13 questions randomly and generating the questions list. 
	
	for i in range(0,len(dictionary_number)):
		my_answer = input(questions[i])  			#### output from the shuffle function items of that list are passed one by one with the index i
		correct_answer = answers[i]      			#### output from the shuffle function #### Shuffling 13 questions randomly and generating the questions list. 
		score = fuzz.ratio(my_answer, correct_answer)
		
		if score >= 80:
			print("\n\tcorrect answer!!\n")
			print(f"your answer: {my_answer}")
			print(f"correct answer: {correct_answer}")
			print(f"\t\nYou score for this answer is: {score}")
			print("Go to the next question")
			correct_answers.append(questions[i])    
		elif score < 80:
			print("\n\tincorrect answer!\n")
			print(f"your answer: {my_answer}")
			print(f"correct answer: {correct_answer}")
			print(f"\t\nYou score for this answer is: {score}")
			print("Go to the next question")
			wrong_answers.append(questions[i])	




####################################################################
##### 1A. CIVICS_TEST_principles_of_american_democracy() ###########
####################################################################
def CIVICS_TEST_principles_of_american_democracy():
	
	run_questions(list_of_dict[0])
		
	print("\n\nEnd of the 1A.CIVICS_TEST_principles_of_american_democracy\n\n")
	
	complete1A = set(correct_answers) | set(wrong_answers) >= dict_quizz1A.keys()
	complete1B = set(correct_answers) | set(wrong_answers) >= dict_quizz1B.keys()
	complete1C = set(correct_answers) | set(wrong_answers) >= dict_quizz1C.keys()

	if complete1A == True and complete1B == True and complete1C == True:
		print("1-CIVICS session ends. Move on to next session 2-AMERICAN HISTORY")
		print("2 - AMERICAN HISTORY")
		print("A: Colonial Period and Independence (questions 58 to 70)")
		print("B: 1800s (questions 71 to 77)")
		print("C: Recent American History and Other Important Historical Information (questions 78 to 87)\n")
	
		move_on = input("What subtopic do you want to select from the AMERICAN HISTORY session? A, B, or C?")
	
		if move_on == "A" or move_on == "a":
			print("A: Colonial Period and Independence (questions 58 to 70)")
			AMERICAN_HISTORY_Colonial_Period_and_Independence()
		elif move_on == "B" or move_on == "b":
			print("B: 1800s (questions 71 to 77)")
			AMERICAN_HISTORY_1800s()
		elif move_on == "C" or move_on == "c":
			print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
			AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
		else:                                                                                                                           
			print("ERROR :::: please select a letter that exists")

	elif complete1A == True and complete1B == True and complete1C == False:
		print("This is the last session for you to CIVICS_TEST session")
		print("1A and 1B is complete, move on to 1C:")	
		print("C: Rights and Responsibilities (questions 48 to 57)")
		CIVICS_TEST_Rights_and_Responsilities()
	
	elif complete1A == True and complete1B == False and complete1C == False:
		move_on = input("What subtopic do you want to select from the CIVIS TEST session? B, or C? >   ")
		if move_on == "B" or move_on == "b":
			print("1A is complete, you are moving on to 1B:")
			print("B: Systems of Government (questions 13 to 47)")
			CIVICS_TEST_systems_of_government()
		elif move_on == "C" or move_on == "c":
			print("1A is complete, you are moving on to 1C:")
			print("C: Rights and Responsibilities (questions 48 to 57)")
			CIVICS_TEST_Rights_and_Responsilities()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	
	elif complete1A == True and complete1B == False and complete1C == True:
		print("This is the last session for you to CIVICS_TEST session")
		print("1A and 1C are both complete, please move on to 1B")	
		print("B: Systems of Government (questions 13 to 47)")
		CIVICS_TEST_systems_of_government()
		
####################################################################
############## 1B. CIVICS_TEST_systems_of_government() #############
####################################################################
def CIVICS_TEST_systems_of_government():

	run_questions(list_of_dict[1])
	
	print("\n\nEnd of the 1B.CIVICS_TEST_systems_of_government\n\n")
	
	
	complete1A = set(correct_answers) | set(wrong_answers) >= dict_quizz1A.keys()
	complete1B = set(correct_answers) | set(wrong_answers) >= dict_quizz1B.keys()
	complete1C = set(correct_answers) | set(wrong_answers) >= dict_quizz1C.keys()

	if complete1A == True and complete1B == True and complete1C == True:
		print("1 - CIVICS session ends. Move on to next session 2 - AMERICAN HISTORY\n\n")
		print("2 - AMERICAN HISTORY")
		print("A: Colonial Period and Independence (questions 58 to 70)")
		print("B: 1800s (questions 71 to 77)")
		print("C: Recent American History and Other Important Historical Information (questions 78 to 87)\n")
	
		move_on = input("What subtopic do you want to select from the AMERICAN HISTORY session? A, B, or C?")
	
		if move_on == "A" or move_on == "a":
			print("A: Colonial Period and Independence (questions 58 to 70)")
			AMERICAN_HISTORY_Colonial_Period_and_Independence()
		elif move_on == "B" or move_on == "b":
			print("B: 1800s (questions 71 to 77)")
			AMERICAN_HISTORY_1800s()
		elif move_on == "C" or move_on == "c":
			print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
			AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
		else:                                                                                                                           
			print("ERROR :::: please select a letter that exists")

	elif complete1A == True and complete1B == True and complete1C == False:
		print("This is the last session for you to CIVICS_TEST session")
		print("1A and 1B is complete, move on to 1C:")	
		print("C: Rights and Responsibilities (questions 48 to 57)")
		CIVICS_TEST_Rights_and_Responsilities()
	
	elif complete1A == False and complete1B == True and complete1C == False:
		move_on = input("What subtopic do you want to select from the CIVIS TEST session? A, or C? >   ")
		if move_on == "A" or move_on == "a":
			print("1B is complete, you are moving on to 1A:")
			print("A: Principles of the American Democracy (questions 1 to 12)")
			CIVICS_TEST_principles_of_american_democracy()
		elif move_on == "C" or move_on == "c":
			print("1B is complete, you are moving on to 1C:")
			print("C: Rights and Responsibilities (questions 48 to 57)")
			CIVICS_TEST_Rights_and_Responsilities()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	elif complete1A == False and complete1B == True and complete1C == True:
		print("This is the last session for you to CIVICS_TEST session")	
		print("1B and 1C are both complete, go ahead and finish session 1A")
		print("A: Principles of the American Democracy (questions 1 to 12)")
		CIVICS_TEST_principles_of_american_democracy()

####################################################################
######### 1C. CIVICS_TEST_Rights_and_Responsibilities() ############
####################################################################
def CIVICS_TEST_Rights_and_Responsilities():
	
	run_questions(list_of_dict[2])
	
	print("\n\nEnd of the 1C.CIVICS_TEST_Rights_and_Responsibilities\n\n")
	
	complete1A = set(correct_answers) | set(wrong_answers) >= dict_quizz1A.keys()
	complete1B = set(correct_answers) | set(wrong_answers) >= dict_quizz1B.keys()
	complete1C = set(correct_answers) | set(wrong_answers) >= dict_quizz1C.keys()

	if complete1A == True and complete1B == True and complete1C == True:
		print("1 - CIVICS session ends. Move on to next session 2 - AMERICAN HISTORY")
		print("2 - AMERICAN HISTORY")
		print("A: Colonial Period and Independence (questions 58 to 70)")
		print("B: 1800s (questions 71 to 77)")
		print("C: Recent American History and Other Important Historical Information (questions 78 to 87)\n")
	
		answer2 = input("What subtopic do you want to select from the AMERICAN HISTORY session? A, B, or C?")
	
		if answer2 == "A" or answer2 == "a":
			print("A: Colonial Period and Independence (questions 58 to 70)")
			AMERICAN_HISTORY_Colonial_Period_and_Independence()
		elif answer2 == "B" or answer2 == "b":
			print("B: 1800s (questions 71 to 77)")
			AMERICAN_HISTORY_1800s()
		elif answer2 == "C" or answer2 == "c":
			print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
			AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
		else:                                                                                                                           
			print("ERROR :::: please select a letter that exists")

	elif complete1A == False and complete1B == True and complete1C == True:
		print("This is the last session for you to CIVICS_TEST session")	
		print("A: Principles of the American Democracy (questions 1 to 12)")
		CIVICS_TEST_principles_of_american_democracy()
	
	elif complete1A == False and complete1B == False and complete1C == True:
		move_on = input("What subtopic do you want to select from the CIVIS TEST session? A, or B? >   ")
		if move_on == "A" or move_on == "a":
			print("1B is complete, you are moving on to 1A:")
			print("A: Principles of the American Democracy (questions 1 to 12)")
			CIVICS_TEST_principles_of_american_democracy()
		elif move_on == "B" or move_on == "b":
			print("1A is complete, you are moving on to 1B:")
			print("B: Systems of Government (questions 13 to 47)")
			CIVICS_TEST_systems_of_government()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	elif complete1A == True and complete1B == False and complete1C == True:
		print("This is the last session for you to CIVICS_TEST session")
		print("1A and 1C are both complete, go ahead and finish session 1B")
		print("B: Systems of Government (questions 13 to 47)")
		CIVICS_TEST_systems_of_government()




####################################################################
######  2A. AMERICAN_HISTORY_Colonial_Period_and_Independence() ####
####################################################################
def AMERICAN_HISTORY_Colonial_Period_and_Independence():
	run_questions(list_of_dict[3])
	
	print("\n\nEnd of 2A.AMERICAN_HISTORY_Colonial_Period_and_Independence\n\n")
	
	complete2A = set(correct_answers) | set(wrong_answers) >= dict_quizz2A.keys()
	complete2B = set(correct_answers) | set(wrong_answers) >= dict_quizz2B.keys()
	complete2C = set(correct_answers) | set(wrong_answers) >= dict_quizz2C.keys()

	if complete2A == True and complete2B == True and complete2C == True:
		print("1 - AMERICAN HISTORY session ends. Move on to next session 3 - INTEGRATED CIVICS")
		print("3 - INTEGRATED CIVICS")
		print("A: Geography (questions 88 to 95)")
		print("B: Symbols (questions 96 to 98")
		print("C: Holidays (questions 99 to 100) \n")
	
		answer3 = input("What subtopic do you want to select from the INTEGRATED CIVICS session? A, B, or C?")
	
		if answer3 == "A" or answer3 == "a":
			print("A: Geography (questions 88 to 95)")
			INTEGRATED_CIVICS_Geography()
		elif answer3 == "B" or answer3 == "b":
			print("B: Symbols (questions 96 to 98")
			INTEGRATED_CIVICS_Symbols()
		elif answer3 == "C" or answer3 == "c":
			print("C: Holidays (questions 99 to 100)")
			INTEGRATED_CIVICS_Holidays()
		else:
			print("ERROR :::: please select a letter that exists")

	elif complete2A == True and complete2B == True and complete2C == False:
		print("This is the last session AMERICAN HISTORY")
		print("2A and 2B are complete, move on to 2C:")	
		print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
		AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
	
	elif complete2A == True and complete2B == False and complete2C == False:
		move_on = input("What subtopic do you want to select from the AMERICAN HISTORY session? B, or C? >   ")
		if move_on == "B" or move_on == "b":
			print("2A is complete, you are moving on to 2B:")
			print("B: 1800s (questions 71 to 77)")
			AMERICAN_HISTORY_1800s()
		elif move_on == "C" or move_on == "c":
			print("2A is complete, you are moving on to 2C:")
			print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
			AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	
	elif complete2A == True and complete2B == False and complete2C == True:
		print("This is the last session for you to AMERICAN HISTORY session")
		print("2A and 2C are both complete, please move on to 2B")	
		print("B: 1800s (questions 71 to 77)")
		AMERICAN_HISTORY_1800s()
		
####################################################################
################# 2B. AMERICAN_HISTORY_1800s()######################
####################################################################
def AMERICAN_HISTORY_1800s():
	run_questions(list_of_dict[4])
	
	print("\n\nEnd of 2B.AMERICAN_HISTORY_1800s\n\n")
	
	complete2A = set(correct_answers) | set(wrong_answers) >= dict_quizz2A.keys()
	complete2B = set(correct_answers) | set(wrong_answers) >= dict_quizz2B.keys()
	complete2C = set(correct_answers) | set(wrong_answers) >= dict_quizz2C.keys()

	if complete2A == True and complete2B == True and complete2C == True:
		print("1 - AMERICAN HISTORY session ends. Move on to next session 3 - INTEGRATED CIVICS")
		print("3 - INTEGRATED CIVICS")
		print("A: Geography (questions 88 to 95)")
		print("B: Symbols (questions 96 to 98")
		print("C: Holidays (questions 99 to 100) \n")
	
		answer3= input("What subtopic do you want to select from the INTEGRATED CIVICS session? A, B, or C?")
	
		if answer3 == "A" or answer3 == "a":
			print("A: Geography (questions 88 to 95)")
			INTEGRATED_CIVICS_Geography()
		elif answer3 == "B" or answer3 == "b":
			print("B: Symbols (questions 96 to 98")
			INTEGRATED_CIVICS_Symbols()
		elif answer3 == "C" or answer3 == "c":
			print("C: Holidays (questions 99 to 100)")
			INTEGRATED_CIVICS_Holidays()
		else:
			print("ERROR :::: please select a letter that exists")

	elif complete2A == True and complete2B == True and complete2C == False:
		print("This is the last session AMERICAN HISTORY")
		print("2A and 2B are complete, move on to 2C:")	
		print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
		AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
	
	elif complete2A == False and complete2B == True and complete2C == False:
		move_on = input("What subtopic do you want to select from the AMERICAN HISTORY session? A, or C? >   ")
		if move_on == "A" or move_on == "a":
			print("2B is complete, 2A and 2C are not, you choose move on to 2A first:")
			print("A: Colonial Period and Independence (questions 58 to 70)")
			AMERICAN_HISTORY_Colonial_Period_and_Independence()
		elif move_on == "C" or move_on == "c":
			print("2B is complete, 2A and 2C are not, you choose move on to 2C first:")
			print("C: Recent American History and Other Important Historical Information (questions 78 to 87)")
			AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	elif complete2A == False and complete2B == True and complete2C == True:
		print("This is the last session for you to AMERICAN HISTORY session")
		print("2B and 2C are both complete, please move on to 2A")	
		print("A: Colonial Period and Independence (questions 58 to 70)")
		AMERICAN_HISTORY_Colonial_Period_and_Independence()
		
###################################################################################################
#### 2C. AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information() ####
###################################################################################################
def AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information():
	run_questions(list_of_dict[5])
	
	print("\n\nEnd of 2C.AMERICAN_HISTORY_Recent_American_History_and_Other_Important_Historical_Information\n\n")
	
	complete2A = set(correct_answers) | set(wrong_answers) >= dict_quizz2A.keys()
	complete2B = set(correct_answers) | set(wrong_answers) >= dict_quizz2B.keys()
	complete2C = set(correct_answers) | set(wrong_answers) >= dict_quizz2C.keys()

	if complete2A == True and complete2B == True and complete2C == True:
		print("1 - AMERICAN HISTORY session ends. Move on to next session 3 - INTEGRATED CIVICS")
		print("3 - INTEGRATED CIVICS")
		print("A: Geography (questions 88 to 95)")
		print("B: Symbols (questions 96 to 98")
		print("C: Holidays (questions 99 to 100) \n")
	
		move_on = input("What subtopic do you want to select from the INTEGRATED CIVICS session? A, B, or C?")
	
		if move_on == "A" or move_on == "a":
			print("A: Geography (questions 88 to 95)")
			INTEGRATED_CIVICS_Geography()
		elif move_on == "B" or move_on == "b":
			print("B: Symbols (questions 96 to 98")
			INTEGRATED_CIVICS_Symbols()
		elif move_on == "C" or move_on == "c":
			print("C: Holidays (questions 99 to 100)")
			INTEGRATED_CIVICS_Holidays()
		else:
			print("ERROR :::: please select a letter that exists")

	elif complete2A == True and complete2B == False and complete2C == True:
		print("This is the last session AMERICAN HISTORY")
		print("2A and 2C are complete, move on to 2B:")	
		print("B: 1800s (questions 71 to 77)")
		AMERICAN_HISTORY_1800s()
	
	elif complete2A == False and complete2B == False and complete2C == True:
		move_on = input("What subtopic do you want to select from the AMERICAN HISTORY session? A, or B? >   ")
		if move_on == "A" or move_on == "a":
			print("2C is complete, 2A and 2B are not, you choose move on to 2A first:")
			print("A: Colonial Period and Independence (questions 58 to 70)")
			AMERICAN_HISTORY_Colonial_Period_and_Independence()
		elif move_on == "B" or move_on == "b":
			print("2C is complete, 2A and 2B are not, you choose move on to 2B first:")
			print("B: 1800s (questions 71 to 77)")
			AMERICAN_HISTORY_1800s()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	
	elif complete2A == False and complete2B == True and complete2C == True:
		print("This is the last session for you to AMERICAN HISTORY session")
		print("2B and 2C are both complete, please move on to 2A")	
		print("A: Colonial Period and Independence (questions 58 to 70)")
		AMERICAN_HISTORY_Colonial_Period_and_Independence()



	
####################################################################
########## 3A. INTEGRATED_CIVICS_Geography()########################
####################################################################
def INTEGRATED_CIVICS_Geography():
	run_questions(list_of_dict[6])
	
	print("\n\nEnd of 3A.INTEGRATED_CIVICS_Geography\n\n")
	
	complete3A = set(correct_answers) | set(wrong_answers) >= dict_quizz3A.keys()
	complete3B = set(correct_answers) | set(wrong_answers) >= dict_quizz3B.keys()
	complete3C = set(correct_answers) | set(wrong_answers) >= dict_quizz3C.keys()

	if complete3A == True and complete3B == True and complete3C == True:
		print("3 - INTEGRATED CIVICS ends. You have completed the quizz!! Congrats!")

	elif complete3A == True and complete3B == True and complete3C == False:
		print("This is the last session for you to INTEGRATED_CIVIS session")
		print("3A and 3B is complete, move on to 3C:")	
		print("C: Holidays (questions 99 to 100)")
		INTEGRATED_CIVICS_Holidays()
	
	elif complete3A == True and complete3B == False and complete3C == False:
		move_on = input("What subtopic do you want to select from the INTEGRATED HISTORY session? B or C? >   ")
		if move_on == "B" or move_on == "b":
			print("3A is complete, you are moving on to 3B:")
			print("B: Symbols (questions 96 to 98")
			INTEGRATED_CIVICS_Symbols()
		elif move_on == "C" or move_on == "c":
			print("3B is complete, you are moving on to 3C:")
			print("C: Holidays (questions 99 to 100)")
			INTEGRATED_CIVICS_Holidays()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	elif complete3A == True and complete3B == False and complete3C == True:
		print("This is the last session for you to INTEGRATED CIVICS session")
		print("3A and 3C are both complete, please move on to 3B")	
		print("B: Symbols (questions 96 to 98)")
		INTEGRATED_CIVICS_Symbols()
		
####################################################################
###########3B. INTEGRATED_CIVICS_Symbols()##########################
####################################################################
def INTEGRATED_CIVICS_Symbols():
	run_questions(list_of_dict[7])
	
	print("\n\nEnd of 3B.INTEGRATED_CIVICS_Symbols\n\n")
	
	complete3A = set(correct_answers) | set(wrong_answers) >= dict_quizz3A.keys()
	complete3B = set(correct_answers) | set(wrong_answers) >= dict_quizz3B.keys()
	complete3C = set(correct_answers) | set(wrong_answers) >= dict_quizz3C.keys()

	if complete3A == True and complete3B == True and complete3C == True:
		print("3 - INTEGRATED CIVICS ends. You have completed the quizz!! Congrats!")

	elif complete3A == True and complete3B == True and complete3C == False:
		print("This is the last session of INTEGRATED_CIVIS")
		print("3A and 3B are complete, move on to 3C:")	
		print("C: Holidays (questions 99 to 100)")
		INTEGRATED_CIVICS_Holidays()
	
	elif complete3A == False and complete3B == True and complete3C == False:
		move_on = input("What subtopic do you want to select from the INTEGRATED HISTORY session? A, or C? >   ")
		if move_on == "A" or move_on == "a":
			print("3B is complete, you are moving on to 3A:")
			print("A: Geography (questions 88 to 95)")
			INTEGRATED_CIVICS_Geography()
		elif move_on == "C" or move_on == "c":
			print("3B is complete, you are moving on to 3C:")
			print("C: Holidays (questions 99 to 100)")
			INTEGRATED_CIVICS_Holidays()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	elif complete3A == False and complete3B == True and complete3C == True:
		print("This is the last session for you to INTEGRATED CIVICS session")
		print("3B and 3C are both complete, please move on to 3A")	
		print("A: Geography (questions 88 to 95)")
		INTEGRATED_CIVICS_Geography()
	
####################################################################
###############3C. INTEGRATED_CIVICS_Holidays()#####################
####################################################################
def INTEGRATED_CIVICS_Holidays():
	run_questions(list_of_dict[8])
	
	print("\n\nEnd of 3C.INTEGRATED_CIVICS_Holidays\n\n")
	
	complete3A = set(correct_answers) | set(wrong_answers) >= dict_quizz3A.keys()
	complete3B = set(correct_answers) | set(wrong_answers) >= dict_quizz3B.keys()
	complete3C = set(correct_answers) | set(wrong_answers) >= dict_quizz3C.keys()

	if complete3A == True and complete3B == True and complete3C == True:
		print("3 - INTEGRATED CIVICS ends. You have completed the quizz!! Congrats!")

	elif complete3A == True and complete3B == False and complete3C == True:
		print("This is the last session of INTEGRATED_CIVIS")
		print("3A and 3C are complete, move on to 3B:")	
		print("B: Symbols (questions 96 to 98")
		INTEGRATED_CIVICS_Symbols()
	
	elif complete3A == False and complete3B == False and complete3C == True:
		move_on = input("What subtopic do you want to select from the INTEGRATED HISTORY session? A, or B? >   ")
		if move_on == "A" or move_on == "a":
			print("3C is complete, you are moving on to 3A:")
			print("A: Geography (questions 88 to 95)")
			INTEGRATED_CIVICS_Geography()
		elif move_on == "B" or move_on == "b":
			print("3A is complete, you are moving on to 3B:")
			print("B: Symbols (questions 96 to 98")
			INTEGRATED_CIVICS_Symbols()
		else:
			print("ERROR ::: please select a letter corresponding to a option that exists")
			
	elif complete3A == False and complete3B == True and complete3C == True:
		print("This is the last session for you to INTEGRATED CIVICS session")
		print("3B and 3C are both complete, please move on to 3A")	
		print("A: Geography (questions 88 to 95)")
		INTEGRATED_CIVICS_Geography()
	
	
start()
	
	
