GOLF TIME BOOKER
------------------
VERSION 0.0 --> Functional, but requires some hard coding to get your designated date at the moment. To be fixed in future updates.
VERSION 0.1 --> Functional and now contains the option to input your desired date and time.

ABOUT THIS PROJECT
-----------------
This project utilizes Python with Selenium and PySimpleGUI to create a system which automates the booking of a tee time on the LA county golf website. Many people may find it hard to book certain tee times, which are often booked moments after release. The use of this project aims to reduce checkout time by automating the following processes:

1. The login page
2. Date selection
3. Course selection
4. Time selection
5. Confirmation and checkout (provided a credit card is associated with the account)

While it is not guaranteed that you will get your tee time, this process is much quicker than manually entering your information.


SET-UP
------------------
1. Download the program
	Download Golfer.py and extract it into a folder that has an accessible location (like your Desktop).

2. Open Windows PowerShell
	Look for Windows PowerShell on your searchbar. It should bring up a small terminal.

3. Change your directory to the file location
	My Windows PowerShell defaults to \Users\[my name] . If you stored the folder on your desktop, type this into the terminal:
	cd Desktop
	Once you navigate to the Desktop, type this into terminal:
	cd [name of folder]

4. Install necessary packages and add-ons
	When you navigate into the folder location, you will need to first install python 3. Check this link on how to install python (any version above Python 3 should do)
	https://phoenixnap.com/kb/how-to-install-python-3-windows (MAKE SURE YOU ADD PIP AND PYTHON TO YOUR PATH! Otherwise you may run into trouble using pip later on.)

	You don't need to do the optional steps. Next, you will need to use pip to install some add-ons. Type the following into your console:
	pip install selenium
	pip install webdriver_manager
	pip install PySimpleGUI

	If you run into problems using these commands, try using pip3 instead.

5. Download Chrome (if you don't have it already)

6. Run the program
	The program should be ready to run now. To run the program, type the following into the command line:
	python3 Golfer.py


NOTES
--------------
Upon running the first time, the program will ask you to enter your ID. Your ID will be saved to user.txt, so don't change anything in there or else login may fail.
You can set the program to run exactly at 6 am using the Task Scheduler, but you will still need to click "Ok" for the program to start running.
The confirmation window was added to avoid any trouble with accidental charges; ONLY click "Ok" on the final warning if you're ready to book a time. The program also assumes
you have a credit card added to your account already.

On first time setup, you need to input a date and time. On future startups, you will be asked if you want to change your date and time. If you don't want to change, you can simply
leave the fields blank. 

If you want the program to run with Task Scheduler, follow these steps:

1. Search Task Scheduler on your PC search bar
2. On the right hand side, click "Create basic task"
3. Name your task and select "One time". You can choose as many times as you want, but Version 0.0 only supports one date, so it won't work if you set it to occur daily.
4. Change to appropriate date at 6am
5. Click "run a program"
6. Click browse and navigate to the folder with the Golfer file. Then, select Golfer.py to be the script run.
7. Click finish, and the program should execute at the given time as long as your computer is on.

Also, make sure you're checking the PowerShell if things seem to freeze up. There's little messages that appear when a task has been successful or a failure. 


KNOWN ISSUES
-------------
-Sometimes the program may take too long to load and will error out. If this happens, try running again. If the error occurs again, the time has probably been booked already.


TO-DO LIST
------------
- Desired courses can not currently be edited. This will be updated in the next patch so you can add and manipulate your preferences. 
- Going to add in a reject message and exit if the wrong input is put in for a date or time. 
- Going to divide the code up into smaller functions so that things are a bit cleaner.
- For cleaning purposes, I may not search for elements using their full XPATH any more. 
- Going to add a trial/demonstration version which proceeds to the confirmation page, but doesn't hit checkout.
- May develop a separate version which assumes the user is already logged in and has all of their prefences selected; all that would occur is the search for an appropriate time,   the confirmation, and checkout. 
