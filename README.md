# ACB-GUI-Feature-Addition
	•	install required modules eg. pymysql, sqlalchemy
	•	manually create a database in MySQL server and configure MySQL server if required
	•	Please name your database as acbtask1 as many variables in the code are dependent on this
		in ACB.py and CombineOutputs.py , the line where the sqlalchemy engine is initialised has to be appropriately changed : alter the username, password(shown as xxxx), IP address(currently localhost), database name(database which will be used)
	•	run the ui.py and ACB.py files. The GUI will appear
	•	finish course allotment for each student following the same procedure as before. 
	•	When a particular course is selected, the number of students registered for each section shows up next to each section under ‘Click to add section’
	•	Most of the original logic and code has been retained as is. New code has been explained using comments
	•	For task1: MySQL has been used. Amongst all the excel files involved - Timetable, Pre-requisite, Registration data(used for student count in each section), ACB Backlog — I have assumed all of these to be static and pre-computed and hence have left them as is in excel format and code also deals with them in excel format
	•	The "Pending Backlog" and the various stu_op20xxxxxxx files are now accessed using and stored as tables in a single MySQL database (the python code handles this). These are not stored or used as excel files. Currently, no python code has been written to view the final course registrations for each student, but this functionality can be easily added  
	•	By changing ‘localhost’ to an IP address for an online server and changing the username and password, the same code should be able to support the requirements of task1 - sync across multiple users.
	•	For task2 - the ‘Registration Data’ excel file has been used to find the number of students enrolled in each section. Optimisation for speed has been achieved by using a dictionary to pre-compute and store the student count for each section of each course
	•	if a course has zero registrations, it shows ‘Course not offered this sem’ : has to be dealt with manually maybe in cases like registration for a project course
	•	pool_recycle may have to be added for the sqlalchemy engine based on usage
	•	Plan for: debugging the issue of Timetable not displaying properly when the software is used multiple times: can be done via testing and finding the cases which generate bugs and hence identifying faulty code followed by debugging
