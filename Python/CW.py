# This is same CW in CMJD create using python

import os

# All student details list
# Three data sets have been added as demo data
studentDetailsList = [["S001","S002","S003"],["Lahiru","Rashmitha","Kamal"],[-1,50,60],[-1,70,90]]
""" 
[0] = Student ID
[1] = Student name
[2] = Programming marks
[3] = Database management system marks
"""

# Menu name ---------------------------------------------------------------------
def menuName(name):
	# Mainmenu name 
	for i in range(90):
		print("-", end="")
		
	size = len(name)
	size = (88 - size) // 2
	
	print("\n|", end="")
	for i in range(size):
		print(" ", end="")
	print(name,end="")
	for i in range(size):
		print(" ", end="")
	print("|")
		
	for i in range(90):
		print("-" ,end="")
	print("\n")

# Chack ID ----------------------------------------------------------------------
def chekID(ID):
	
	# Check ID is in database or not
	if ID in studentDetailsList[0]:
		return True
	else:
		return False

# Mani menu funshan(method) -----------------------------------------------------
def mainMenu():
	
	# Mainmenu name 
	menuName("Welcom To GDSE Marks Management System")
	
	# Mainmenu options
	print(" [1] Add New Student\t\t\t [2] Add New Student With Marks")
	print(" [3] Add Marks\t\t\t\t [4] Update Student Details")
	print(" [5] Update Marks\t\t\t [6] Delete Student")
	print(" [7] Print Student Details\t\t [8] Print Student Ranks")
	print(" [9] Best In Programming Fundamentals\t[10] Best In Database Management System")
	print("[11] Exit\n")
	
	# get user ans
	try:
		x = int(input(">>>>> Enter an option to continue > "))
		if x <= 0 or x > 11:
			print("\tEnter correct menu number !\n")
			return -1
			
		else:
			return x
		
	except ValueError as ex:
		print("\tInvalide data type\n\tEnter integer value !\n")
		return -1
	except Exception as ex:
		print(ex.getMessage())
		return -1

# [1] Add New Student funshan(method) -------------------------------------------
def addStudent():
	
	# Menu name 
	menuName("Add New Student ")
	
	# Get student details
	loopBreak = True
	
	while loopBreak:
		ID = input("Enter Student ID   > ").upper()
		
		if chekID(ID):
			print("\tThis student ID is already exists !\n")
		
		elif ID == "":
			print("\tEnter ID Correctly !\n")
		
		else:
			while True:
				name = input("Enter Student Name > ")
			
				if name == "":
					print("\tEnter Name Correctly !\n")
				
				else:
					studentDetailsList[0].append(ID)
					studentDetailsList[1].append(name)
					studentDetailsList[2].append(-1)
					studentDetailsList[3].append(-1)
					print("\nStudent has been added successfully .....")
					
					while True:
						userInput = input("Do you want to add a new student (Y/N) > ").upper()
						print("")
						if userInput == "N" or userInput == "NO":
							os.system("cls")
							loopBreak = False
							break
							
						elif userInput == "Y" or userInput == "YES":
							break
					break

# [2] Add New Student With Marks ------------------------------------------------
def addStudentWithMarks():
	
	# Menu name 
	menuName("Add New Student With Marks")
	
	# Get student details
	loopBreak = True
	
	while loopBreak:
		ID = input("Enter Student ID   > ").upper()
		
		if chekID(ID):
			print("\tThis student ID is already exists !\n")
		
		elif ID == "":
			print("\tEnter ID Correctly !\n")
			
		else:
			while True:
				name = input("Enter Student Name > ")
				
				if name == "":
					print("\tEnter Name Correctly !\n")
			
				else:
					studentDetailsList[0].append(ID)
					studentDetailsList[1].append(name)

					while True:
						try:
							proMarks = float(input("Programming Fundamentals Marks   > "))
							studentDetailsList[2].append(proMarks)
							break

						except ValueError as ex:
							print("\tEnter Integer or Float Value !\n")

					while True:
						try:
							dbmsMarks = float(input("Database Management System Marks > "))
							studentDetailsList[3].append(dbmsMarks)
							break

						except ValueError as ex:
							print("\tEnter Integer or Float Value !\n")

					print("\nStudent has been added successfully .....")
						
					while True:
						userInput = input("Do you want to add a new student (Y/N) > ").upper()
						print("")
						if userInput == "N" or userInput == "NO":
							os.system("cls")
							loopBreak = False
							break

						elif userInput == "Y" or userInput == "YES":
							break
					break

# [3] Add Marks -----------------------------------------------------------------
def addMarks():

	# Menu name
	menuName("Add Marks ")

	# Add student marks
	loopBreak = True
	while loopBreak:
		ID = input("Enter Student ID > ").upper()

		if chekID(ID):
			print("Student Name >",studentDetailsList[1][studentDetailsList[0].index(ID)])
			pro = studentDetailsList[2][studentDetailsList[0].index(ID)]
			dbms = studentDetailsList[3][studentDetailsList[0].index(ID)]

			if pro != -1 or dbms != -1:
				print("\tThis student's marks have been already added !")
				print("\tIf you want to update the marks, please use [5] Update Marks option !")

				while True:
					userInput = input("\tDo you want to add marks for another student (Y/N)? > ").upper()
					print("")

					if userInput == "N" or userInput == "NO":
						loopBreak = False
						break

					elif userInput == "Y" or userInput == "YES":
						break

			else:
				while True:
					try:
						newPro = float(input("Programming Fundamentals Marks > "))
						if newPro >= 0 and newPro <= 100:
							studentDetailsList[2][studentDetailsList[0].index(ID)] = newPro
							break
						else:
							print("\tInvalid Marks, Please Enter Correct Marks !\n")

					except ValueError as ex:
						print("\tEnter Integer or Float value !\n")

				while True:
					try:
						newDbms = float(input("Database Management System Marks > "))
						if newDbms >= 0 and newDbms <= 100:
							studentDetailsList[3][studentDetailsList[0].index(ID)] = newDbms
							break
						else:
							print("\tInvalid Marks, Please Enter Correct Marks !\n")

					except ValueError as ex:
						print("\tEnter Integer or Float value !\n")

				print("\tMarks have been added successfully .....")

				while True:
					userInput = input("\tDo you want to add marks for another student (Y/N)? > ").upper()
					print("")

					if userInput == "N" or userInput == "NO":
						loopBreak = False
						break

					elif userInput == "Y" or userInput == "YES":
						break

		else:
			print("\tInvalid Student ID")

			while True:
				userInput = input("\tDo you want to search again (Y/N)? > ").upper()
				print("")

				if userInput == "N" or userInput == "NO":
					loopBreak = False
					break

				elif userInput == "Y" or userInput == "YES":
					break

# [4] Update Student Details ----------------------------------------------------
def updateStudentDetails():

	# Menu name
	menuName("Update Student Details")

	# Update student details
	loopBreak = True

	while loopBreak:
		ID = input("Enter Student ID > ").upper()

		if chekID(ID):
			print("Student name >", studentDetailsList[1][studentDetailsList[0].index(ID)])

			while True:
				newName = input("Enter new student name > ")

				if newName == "":
					print("\tEnter name correctly !\n")
				else:
					studentDetailsList[1][studentDetailsList[0].index(ID)] = newName
					print("Student details has been update Successfully .....")

					while True:
						userInput = input("Do you want to update student details again (Y/N)? > ").upper()
						print("")

						if userInput == "N" or userInput == "NO":
							loopBreak = False
							break

						elif userInput == "Y" or userInput == "YES":
							break

					break

		else:
			print("\tInvalid Student ID !")
			while True:
				userInput = input("Do you want to search again (Y/N)? > ").upper()
				print("")

				if userInput == "N" or userInput == "NO":
					loopBreak = False
					break

				elif userInput == "Y" or userInput == "YES":
					break

# [5] Update Student Details ----------------------------------------------------
def updateMarks():

	# Menu name
	menuName("Update Marks")

	# Update marks
	loopBreak = True;

	while loopBreak:
		ID = input("Enter Student ID > ").upper()

		if chekID(ID):
			pro = studentDetailsList[2][studentDetailsList[0].index(ID)]
			dbms = studentDetailsList[3][studentDetailsList[0].index(ID)]

			if pro == -1 or dbms == -1:
				print("\tThis student's marks yet to be added !")

				while True:
					userInput = input("Do you want to update the marks of another student (Y/N)? > ").upper()
					print("")

					if userInput == "N" or userInput == "NO":
						loopBreak = False
						break

					elif userInput == "Y" or userInput == "YES":
						break

			else:
				print("Student name >", studentDetailsList[1][studentDetailsList[0].index(ID)])
				print("Programming Fundamentals marks >", pro)
				print("Database Management System marks >", dbms, "\n")

				while True:
					try:
						newPro = float(input("Enter new Programming Fundamentals Marks > "))
						if newPro >= 0 and newPro <= 100:
							studentDetailsList[2][studentDetailsList[0].index(ID)] = newPro
							break
						else:
							print("\tInvalid Marks, Please Enter Correct Marks !\n")

					except ValueError as ex:
						print("\tEnter Integer or Float value !\n")

				while True:
					try:
						newDbms = float(input("Enter new Database Management System Marks > "))
						if newDbms >= 0 and newDbms <= 100:
							studentDetailsList[3][studentDetailsList[0].index(ID)] = newDbms
							break
						else:
							print("\tInvalid Marks, Please Enter Correct Marks !\n")

					except ValueError as ex:
						print("\tEnter Integer or Float value !\n")

				print("\tMarks have been added successfully .....")

				while True:
					userInput = input("Do you want to update the marks of another student (Y/N)? > ").upper()
					print("")

					if userInput == "N" or userInput == "NO":
						loopBreak = False
						break

					elif userInput == "Y" or userInput == "YES":
						break

		else:
			print("\tInvalid Student ID !")
			while True:
				userInput = input("Do you want to search again (Y/N)? > ").upper()
				print("")

				if userInput == "N" or userInput == "NO":
					loopBreak = False
					break

				elif userInput == "Y" or userInput == "YES":
					break

# [6] Delete Student ------------------------------------------------------------
def deleteStudent():

	# Menu name
	menuName("Delete Student")

	# Update student
	loopBreak = True

	while loopBreak:
		ID = input("Enter Student ID do you want to Delete > ").upper()

		if chekID(ID):
			pro = studentDetailsList[2][studentDetailsList[0].index(ID)]
			dbms = studentDetailsList[3][studentDetailsList[0].index(ID)]

			print("Student name >",studentDetailsList[1][studentDetailsList[0].index(ID)])
			if pro == -1 or dbms == -1:
				print("Marks did not update yet")
			else:
				print("Programming Fundamentals marks >", pro)
				print("Database Management System marks >", dbms)

			while True:
				userInput = input("Are you sure do you want to Delete this Student (Y/N)? > ").upper()
				print("")

				if userInput == "N" or userInput == "NO":
					loopBreak = False
					break

				elif userInput == "Y" or userInput == "YES":
					del studentDetailsList[1][studentDetailsList[0].index(ID)]
					del studentDetailsList[2][studentDetailsList[0].index(ID)]
					del studentDetailsList[3][studentDetailsList[0].index(ID)]
					del studentDetailsList[0][studentDetailsList[0].index(ID)]

					while True:
						userInput = input("Do you want to search again (Y/N)? > ").upper()
						print("")

						if userInput == "N" or userInput == "NO":
							loopBreak = False
							break

						elif userInput == "Y" or userInput == "YES":
							break

					break


		else:
			print("\tInvalid Student ID !")
			while True:
				userInput = input("Do you want to search again (Y/N)? > ").upper()
				print("")

				if userInput == "N" or userInput == "NO":
					loopBreak = False
					break

				elif userInput == "Y" or userInput == "YES":
					break

# [7] Print Student Details -----------------------------------------------------
def printStudent():

	# Menu name
	menuName("Print Student Details ")

	# Print Student Details
	loopBreak = True

	while loopBreak:
		ID = input("Enter Student ID > ").upper()

		if chekID(ID):
			pro = studentDetailsList[2][studentDetailsList[0].index(ID)]
			dbms = studentDetailsList[3][studentDetailsList[0].index(ID)]

			print("Student name >", studentDetailsList[1][studentDetailsList[0].index(ID)])
			if pro == -1 or dbms == -1:
				print("Marks did not update yet")

			else:
				tempTotal = []
				for x in range(len(studentDetailsList[0])):
					total = studentDetailsList[2][x] + studentDetailsList[3][x]
					if total != -2:
						tempTotal.append(total)

				rank = 0
				tempTotal.sort(reverse=True)
				if (pro+dbms) in tempTotal:
					rank = tempTotal.index(pro+dbms) + 1

				print("+----------------------------------------+----------+")
				print("|%-40s|%10.2f|" % ("Programming Fundamentals marks", pro))
				print("|%-40s|%10.2f|" % ("Database Management System marks",dbms))
				print("|%-40s|%10.2f|" % ("Total Marks", pro+dbms))
				print("|%-40s|%10.2f|" % ("Avg. Marks", (pro+dbms)/2))
				print("|%-40s|%10d|" % ("Rank", rank))
				print("+----------------------------------------+----------+")


			while True:
				userInput = input("\nDo you want to search again (Y/N)? > ").upper()
				print("")

				if userInput == "N" or userInput == "NO":
					loopBreak = False
					break

				elif userInput == "Y" or userInput == "YES":
					break

		else:
			print("\tInvalid Student ID !")
			while True:
				userInput = input("Do you want to search again (Y/N)? > ").upper()
				print("")

				if userInput == "N" or userInput == "NO":
					loopBreak = False
					break

				elif userInput == "Y" or userInput == "YES":
					break

# [8] Print Student Ranks -------------------------------------------------------
def studentRanks():

	# Menu name
	menuName("Print Student's Ranks ")

	# Print Student's Ranks
	tempStudentDetailsList = [] # ["ID", "Name", Total]

	# Get student details without marks students
	for x in range(len(studentDetailsList[0])):
		total = studentDetailsList[2][x] + studentDetailsList[3][x]
		if total != -2:
			tempList = [] # ["ID", "Name", Total]
			tempList.append(studentDetailsList[0][x])
			tempList.append(studentDetailsList[1][x])
			tempList.append(total)
			tempStudentDetailsList.append(tempList)

	# Sort temp student details list by reverse order
	tempStudentDetailsList.sort(reverse=True, key=lambda x:x[2])

	print("+-----+-----+---------------+------------+-----------+")
	print("|%-5s|%-5s|%-15s|%-12s|%-11s|" % ("Rank", "ID", "Name", "Total Marks",  "Avg. Marks"))
	print("+-----+-----+---------------+------------+-----------+")

	if len(tempStudentDetailsList) == 0:
		print("|%-52s|" % "No Students Currently Available !")

	else:
		for x in range(len(tempStudentDetailsList)):
			print("|%-5d|%-5s|%-15s|%12.2f|%11.2f|" % (x+1, tempStudentDetailsList[x][0], tempStudentDetailsList[x][1], tempStudentDetailsList[x][2], tempStudentDetailsList[x][2]/2))

	print("+-----+-----+---------------+------------+-----------+\n")

	while True:
		userInput = input("Do you want to back to main menu (Y/N)? > ").upper()
		print("")

		if userInput == "Y" or userInput == "YES":
			break

# [9] The Best In Programming Fundamentals --------------------------------------
def bestPro():

	# Menu name
	menuName("Best In Programming Fundamentals")

	# Print Student's Ranks
	tempStudentDetailsList = []  # ["ID", "Name" , proMarks, dbmsMarks]

	# Get student details without marks students
	for x in range(len(studentDetailsList[0])):
		total = studentDetailsList[2][x] + studentDetailsList[3][x]
		if total != -2:
			tempList = []  # ["ID", "Name" , proMarks, dbmsMarks]
			tempList.append(studentDetailsList[0][x])
			tempList.append(studentDetailsList[1][x])
			tempList.append(studentDetailsList[2][x])
			tempList.append(studentDetailsList[3][x])
			tempStudentDetailsList.append(tempList)

	# Sort temp student details list by reverse order
	tempStudentDetailsList.sort(reverse=True, key=lambda x: x[2])

	print("+-----+---------------+---------+-----------+")
	print("|%-5s|%-15s|%-9s|%-11s|" % ("ID", "Name", "PF Marks", "DBMS Marks"))
	print("+-----+---------------+---------+-----------+")

	if len(tempStudentDetailsList) == 0:
		print("|%-43s|" % "No Students Currently Available !")

	else:
		for x in range(len(tempStudentDetailsList)):
			print("|%-5s|%-15s|%9.2f|%11.2f|" % (tempStudentDetailsList[x][0], tempStudentDetailsList[x][1], tempStudentDetailsList[x][2], tempStudentDetailsList[x][3]))

	print("+-----+---------------+---------+-----------+\n")

	while True:
		userInput = input("Do you want to back to main menu (Y/N)? > ").upper()
		print("")

		if userInput == "Y" or userInput == "YES":
			break

# [10] The Best In Database Management System -----------------------------------
def bestDBMS():

	# Menu name
	menuName("Best In Database Management System")

	# Print Student's Ranks
	tempStudentDetailsList = []  # ["ID", "Name" , dbmsMarks, proMarks]

	# Get student details without marks students
	for x in range(len(studentDetailsList[0])):
		total = studentDetailsList[2][x] + studentDetailsList[3][x]
		if total != -2:
			tempList = []  # ["ID", "Name" , dbmsMarks, proMarks]
			tempList.append(studentDetailsList[0][x])
			tempList.append(studentDetailsList[1][x])
			tempList.append(studentDetailsList[3][x])
			tempList.append(studentDetailsList[2][x])
			tempStudentDetailsList.append(tempList)

	# Sort temp student details list by reverse order
	tempStudentDetailsList.sort(reverse=True, key=lambda x: x[2])

	print("+-----+---------------+-----------+---------+")
	print("|%-5s|%-15s|%-11s|%-9s|" % ("ID", "Name", "DBMS Marks", "PF Marks"))
	print("+-----+---------------+-----------+---------+")

	if len(tempStudentDetailsList) == 0:
		print("|%-43s|" % "No Students Currently Available !")

	else:
		for x in range(len(tempStudentDetailsList)):
			print("|%-5s|%-15s|%11.2f|%9.2f|" % (tempStudentDetailsList[x][0], tempStudentDetailsList[x][1], tempStudentDetailsList[x][2], tempStudentDetailsList[x][3]))

	print("+-----+---------------+-----------+---------+\n")

	while True:
		userInput = input("Do you want to back to main menu (Y/N)? > ").upper()
		print("")

		if userInput == "Y" or userInput == "YES":
			break

# Main part ---------------------------------------------------------------------
while True:
	userInput = mainMenu()
	
	if userInput == 1:
		os.system("cls")
		addStudent()
	
	elif userInput == 2:
		os.system("cls")
		addStudentWithMarks()
	
	elif userInput == 3:
		os.system("cls")
		addMarks()

	elif userInput == 4:
		os.system("cls")
		updateStudentDetails()

	elif userInput == 5:
		os.system("cls")
		updateMarks()

	elif userInput == 6:
		os.system("cls")
		deleteStudent()

	elif userInput == 7:
		os.system("cls")
		printStudent()

	elif userInput == 8:
		os.system("cls")
		studentRanks()

	elif userInput == 9:
		os.system("cls")
		bestPro()

	elif userInput == 10:
		os.system("cls")
		bestDBMS()

	elif userInput == 11:
		os.system("cls")
		exit()
