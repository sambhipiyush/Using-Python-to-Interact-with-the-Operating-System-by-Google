Using Python to Interact with the Operating System
==================================================

by Google

# Module 1
#
## Title: Getting Your Python On

## Getting Ready for Python

### Getting Familiar with the Operating System

* Operating System
	* The __Operating System__ is a software that manages everything that goes on in the computer
	* It __reads__, __writes__, and __deletes__ files from the hard drive
	* It handles
		1. how the processes start
		1. how they interact with each other
		1. how they eventually finish
	* It manages
		1. how memory gets allocated different processes
		1. how network packets are sent and received
		1. how each programming can access the different hardware components
* Two main parts in Operating System
	1. the __kernel__
		* The __kernel__ is the main core of an operating system
		* It talks directly to our hardware and manages our systems resources.
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/kernel_example_diag_image1.png" alt="kernel_example_diag_image1"></a>
			</p>
	1. the __user space__
		* As users, we don't interact with the kernel directly
			* Instead, we interact with the other part of the operating system called the __user space__
		* The User space is basically everything outside of the kernel
		* These are things that we interact with directly, like the __system programs__ and __user interface__
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/user_space_example_diag_image2.png" alt="user_space_example_diag_image2"></a>
			</p>
* When we say __operating system__, we're referring to both the __kernel__ and the __user space__
* The major operating systems using IT today are
	1. Windows
		* The Windows operating system is developed by Microsoft, and is widely used in the business and consumer space
		* Most PCs come with Windows as the default operating system
	1. Mac OS
		* Mac OS is developed by Apple and is mainly used in the consumer space
		* If you purchase any Apple computer, they'll come with Mac OS preloaded
		* The Mac OS kernel and some of its user space are also based on a kernel and User space tools from the Unix family known as BSD
	1. Linux
		* __Linux__ is an __open source__ operating system
			* __Open source software__ is free to share, modify, and distribute
		* Linux is used heavily in business infrastructure
			* Most servers in the world today are running Linux
				* It's also available in the consumer space, although less common
		* __Linux__ itself is actually the __name of the kernel__ originally developed by __Linus Torvalds__
			* Because of the evolution of the rest of the operating system, we typically use Linux to refer to both the kernel and the whole operating system
		* Today, Linux has grown into a huge community effort with developers all over the world contributing to its success
		* Because Linux is __open source__, a lot of different organizations package their own versions of it, unlike Windows or Mac OS which are solely developed by their respective companies
			* We refer to these different flavors of Linux as distributions
		* Some common __Linux distributions__ are
			1. __Ubuntu__
			1. __Debian__
			1. __Red Hat__
		* If you've heard of __Chrome OS__, you may know that it's another operating system based on a __Linux kernel__
			* But unlike other distributions, Chrome OS is usually considered an OS in its own right
		* the __Android__ operating system which is used a lot on smartphones also runs a __Linux kernel__
* __Unix__
	* __Unix__ is an operating system developed back in the __70's__ by __Bell Labs__
	* After its original release, the OS went through a bunch of different versions with different companies releasing variants of it
	* The fundamental ideas of how Linux works today are based on the Unix principles
	* A lot of the tools that we use to interact with the operating system are open source versions of those originally developed for Unix
	* This is why these tools in operating principles are usually referred to as Unix
		* Even though the OS we're using is called Linux
* __Python__
	* Python is a cross-platform language
	* You can use it on Windows, Mac OS, Linux, and even lesser known Unix variants like FreeBSD
	* It's even available on mobile phones
	* Since it's cross-platform, we can use the same Python code to get to our goal on any operating system, whether the goal is opening files, processing text, or managing running processes

### Getting Your Computer Ready for Python

> pip is a cross-platform tool called a package manager used to install, update, or remove external Python modules

* To check whether you already have Python installed on your computer, open a terminal or command prompt and execute the Python command, passing --version as a parameter
		```bash
		>>> python --version
		```
	* Depending on what's installed on your computer, there's a bunch of different things that can happen
		1. It could say it doesn't recognize the command, which means you don't have Python installed
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/python_version_sample3_image5.png" alt="python_version_sample3_image5"></a>
			</p>
		1. It could return a version that starts with the number two, which tells us that you haven't installed but it's Python 2
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/python_version_sample1_image3.png" alt="python_version_sample1_image3"></a>
			</p>
		1. It could return a version that starts with the number three which means, you guessed it you have Python 3 installed
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/python_version_sample2_image4.png" alt="python_version_sample2_image4"></a>
			</p>
	* If running Python --version returns a version starting with two, try running Python 3 --version
			```bash
			>>> python3 --version
			```
		* Your computer could tell you that the command isn't present which means you'll have to install Python 3
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/python_version_sample5_image7.png" alt="python_version_sample5_image7"></a>
			</p>
		* It can return a version that starts with number three which means you already have Python 3 installed
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/python_version_sample4_image6.png" alt="python_version_sample4_image6"></a>
			</p>
* __Python Standard Library__
	* This comes as part of the Python installation and includes modules for the most common tasks you can do with Python
* We can use external modules for a bunch of tasks, like generating PDFs, starting web pages, creating compressed files, interacting with email, and a lot of other things
* When developers write a Python module that they think others might find useful, they publish it in __PyPI__, also known as the **Py**thon **P**ackage **I**ndex
	* We can browse as repository of Python modules to find the module we need
		* It includes thousands of projects which are classified by different **categories**, like **topic**, **development studies**, and **intended audience**
	* These external modules are generally managed with a command line tool called __pip__
		* This is a cross-platform tool so you can use it to **install**, **update**, and **remove** external modules on whichever operating system you're running on your computer
* The name of the __tool to manage a local packages__ will depend on the distribution that you're using
	* It's called
		1. __apt__ on Debian Ubuntu and Linux Mint
		1. __yum__ on Red Hat or CentOS,
		1. __dnf__ on Fedora

## Running Python Locally

### Interpreted vs. Compiled Languages

* Well, when you want to run a program written in traditional programming language like C. The source code is fed into a piece of software called a __compiler__
	* The __compiler__ translates this code into __machine level language__
		* Which means a language specific to the underlying architecture of the computer it's running on
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/compiler_diag_image8.png" alt="compiler_diag_image8"></a>
			</p>
	* The computer can read and execute the machine level code directly
		* This makes compiled program super fast to run, but the compilation process itself can take a bit of time
	* Some examples of commonly use compiled programming languages are C, C++, Go and Rust
* Programs written in interpreted language generally rely on an intermediary program called an __interpreter__
	* These programs use interpreters to execute the instructions specified in the code
		* Rather than running them through a compiler first
	* So this makes the development cycle for a program written in an interpreted language much faster
		* Because its developer doesn't need to wait for the code to be compiled to execute it
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/interpreter_diag_image9.png" alt="interpreter_diag_image9"></a>
			</p>
	* The same code can be read by interpreters running on different operating systems without needing to make any additional changes
	* The tradeoff is that interpreted languages generally run slower than compiled ones
	* Python, Ruby, JavaScript, Bash, and PowerShell are all examples of interpreted programming languages
* The Python interpreter itself is a complied executable that's platform specific, but once you have it installed, you can run your scripts everywhere
				<p align="center">
				  <a href="javascript:void(0)" rel="noopener">
					 <img width=600px  src="notesImages/python_interpreter_diag_image11.png" alt="python_interpreter_diag_image11"></a>
				</p>
* Java and C# are languages that use a mixed approach
	* The code needs to be compiled first, but it gets compiled into intermediate code
	* This means that instead of getting compiled into machine language that's specific for the current operating system, it gets compiled in supportable code that can execute on different platforms
	* We execute this code using a program that's OS specific, the Java virtual machine for Java and the common language runtime for C#
	* For example
		* You have a program that's written in C, and you're running on Windows
			* But you want to run the program on the Linux server
			* To run the program on a different operating system than the one you're currently running on, you need to compile it on the destination OS
				<p align="center">
				  <a href="javascript:void(0)" rel="noopener">
					 <img width=600px  src="notesImages/c_compile_diag_image10.png" alt="c_compile_diag_image10"></a>
				</p>

### How to Run a Python Script

> Inserting a shebang line (such as `#!/usr/bin/env python3`) as the first line tells the operating system what command we want to use to execute the script.

* When we run the Python 3 command, we get an interactive interpreter
	* When we run this command, it prints a bunch of things
		1. First, we're told the version of Python interpreter were running
		1. Then, we get some extra information like which compiler was used to build it
		1. Then some suggestions for commands that we can use to get more information
				<p align="center">
				  <a href="javascript:void(0)" rel="noopener">
					 <img width=600px  src="notesImages/python_interactive_interpreter_image12.png" alt="python_interactive_interpreter_image12"></a>
				</p>
	* Using the interactive interpreter, we can do everything we learned so far
		```python
		>>> 'hello ' * 2
			hello hello 
		```
	* Unfortunately, we can't save any of our work using interactive interpreter
		* Once you close the interpreter by typing __exit__ or pressing __control+D__ on Linux and Mac OS or __control+Z__ on Windows, the code you wrote isn't even saved
* Saved Python scripts usually end with a `.py` extension such as hello_world.py
* the __cat__ command - It is a command that shows the contents of a file on Linux
* To run a Python script saved
	1. On a Windows system, you can just type the name of your script and the operating system will recognize as the pipeline executable from the file extension
	1. On Linux and Mac OS, you can execute the script by calling the pipeline interpreter followed by the name of the file
			```bash
			>>> cat hello_world.py
				print('Hello, World')
			>>>
			>>> python3 hello_world.py
				Hello, World
			```
		* So here the Python 3 command, the same Python interpreter as before, reads the contents of hello_world.py and then tells the computer to execute the instructions in that file
* We can add the extra line to our file called __shebang__, which tells the operating system what command we want to use to execute that script ( this will help us avoid writing __python3__ everytime to run the script)
	* __shebang__ looks like `#!/usr/bin/env python3` (varies with python version and path of where it is installed)
				<p align="center">
				  <a href="javascript:void(0)" rel="noopener">
					 <img width=600px  src="notesImages/shebang_sample_image13.png" alt="shebang_sample_image13"></a>
				</p>
	* Our system now knows it should execute the file with a Python 3 interpreter
		* We need to make that file executable using the chmod command
			* __chmod__ command lets us change the file permissions
		* To run the file directly, we want our file to be executable
			```bash
			>>> chmod +x hello_world.py
			```
		* Marking the script as executable means that we can now run the file by just prefixing it with a __dot forward-slash__ `./`
			* This means that running `./hello_world.py` is equivalent to `python3 hello_world.py`
			* This approach works exactly the same for both __Linux__ and __Mac OS__
				```bash
				>>> ./hello_world.py
					Hello, World
				```
				<p align="center">
				  <a href="javascript:void(0)" rel="noopener">
					 <img width=600px  src="notesImages/execute_w_shebang_image14.png" alt="execute_w_shebang_image14"></a>
				</p>
			* why we need to prefix the script with a dot slash instead of just writing the name of the script
				* The reason for this is that script isn't located in any of the directories listed in the path variable
				* This variable tells operating system where to find programs to execute
				* The __dot__ in the __dot forward-slash__ expression represents the __current directory__
					* So we're basically telling the OS to find script in the current directory and then execute it

### Your Own Python Modules

> We use the __import__ command to import any module located in the __PATH directory__. We can also use __import__ as to assign a __localName variable__ to the __imported module__

* In programming, we often reuse code that we've written or someone else has written
	* This is called __code reuse__ and nearly all languages provide some way of doing it
* __Functions__ let us group code into logical blocks that can be executed at a later point and as many times as we need
* As our scripts get bigger and more complicated, we want to be able to reuse more than a single function
	* We might even want to reuse entire scripts and other programs that we write
* Cons of duplicating code
	1. First, every time you need to make a change to either script, you have to remember to do it to both places
		* That means you'd have to do any updates and bug fixes twice
	1. On top of this, if your coworkers want to use the same e-mail code you wrote for their own projects, they'd probably have to go and create new copies
		* As you can imagine, keeping track of all the places it's being copied too quickly becomes tricky and so does sharing different versions
* __Module__
	* So instead of maintain a bunch of different copies of the code, we can put the code we want to reuse into a separate __module__
		* This way, we can have our scripts in our colleague scripts import our code without having to create multiple copies
	* To use a __module__, we'll import it using the filename
		* We can access each function, class, and variable defined in the file by using dot notation
	* For Example
		* We have a file called `areas.py` which contains functions to calculate the area of different geometrical figures
		* We can see the contents of that file using cat command
			* We have three functions to find in this module
				* The circle function uses the math.pi constant
					* That's why we import the math module at the top so that we can use it
						<p align="center">
						  <a href="javascript:void(0)" rel="noopener">
							 <img width=600px  src="notesImages/areas_py_content_cat_image15.png" alt="areas_py_content_cat_image15"></a>
						</p>
		* To use them in an interpreter or script, we can import the module by typing `import areas`
			```python
			>>> import area
			```
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/import_areas_py_module_image16.png" alt="import_areas_py_module_image16"></a>
			</p>
		* Let's calculate the area of a triangle and a circle to test this out
			```python
			>>> import areas
			>>> 
			>>> areas.triangle(3, 5)
				7.5
			>>>
			>>> areas.circle(4)
				50.26548246
			```
	* In some cases, the code we're working with can become more complex
		* It might make sense to split into __submodules__
		* In this case, we create a directory with the name of the module, and separate __py__ files for each of the submodules
		* Example: Looking at __request module__
				<p align="center">
				  <a href="javascript:void(0)" rel="noopener">
					 <img width=600px  src="notesImages/request_module_submodule_image17.png" alt="request_module_submodule_image17"></a>
				</p>
			* Notice that `__init__.py` file
				* This is a special file
					* It's red when the module gets imported and it's used by the interpreter to check if a directory with Python files should it be a module
		* So if you have a module split into separate files, and you want the interpreter to recognize the directory has a module, you'll need to create the `__init__.py` file
			* If you don't have anything to put in this file, you need to create it
			* You can leave it __empty__ but it needs to exist for the interpreter to recognize directory as a Python module

### What is an IDE?

* __IDE__ stands for **I**ntegrated **D**evelopment **E**nvironment, and usually refers to a code editor with some handy extra capabilities that make writing scripts a lot easier
	* We do most of our programming work in code editors and IDEs
	* It's a good idea to invest some time now and getting to know a few editors and IDE's to find the one that you like best
* Some have only a few additional features while others have a lot
	1. One of the most basic extra features in code editors is called __Syntax Highlighting__
		* This means that the editor recognizes the language we are writing our code in, and highlights the pieces of code that make up the syntax of the language
		* Example
			* __Vim__
				* Vim includes syntax highlighting
					* So if we open the area's.py file that we showed earlier inside Vim, we'll see that the code includes colors highlighting the syntax
				* We can see that reserved keywords like __def__ or __return__ are shown in one color, while the __names of the functions__ are in a different color, and even numbers are in another color
				* To exit them, type __`:q`__
					<p align="center">
					  <a href="javascript:void(0)" rel="noopener">
						 <img width=600px  src="notesImages/vim_syntax_highlight_image18.png" alt="vim_syntax_highlight_image18"></a>
					</p>
	1. Another common feature offered by code editors is called __Code Completion__
		* **Atom**
			* We have our areas module opened in Atom
			* We see that it also uses syntax highlighting. The colors are different, but the idea is the same
			* let's start a new function called doughnut, which will calculate the area of a 2-D doughnut as the difference between two circles
				* When we type def, the editor tells us that this is a keyword to write a new function
				* After typing the name of the function, we read the opening parentheses, and the editor knows that there will be a closing parentheses so it writes it for us
				* After defining the function when we press Enter, the editor knows that the code needs to be indented to the right
					* So automatically positions the cursor right there
						<p align="center">
						  <a href="javascript:void(0)" rel="noopener">
							 <img width=600px  src="notesImages/atom_code_completion_image19.png" alt="atom_code_completion_image19"></a>
						</p>
				* Now, when I type ret, editor suggests that I may want to type return
					* By pressing tab, I accept the suggestion, and so my ret gets completed to return
						<p align="center">
						  <a href="javascript:void(0)" rel="noopener">
							 <img width=600px  src="notesImages/atom_code_completion_ret_image20.png" alt="atom_code_completion_ret_image20"></a>
						</p>
				* Save with __Control+S__ and close our program with __Control+Q__
* More advanced code editor like __Atom__, __Notepad++__, or __Sublime Text__
* Fully featured graphical IDE like __Eclipse__ or __PyCharm__
* Graphical code editors with additional capabilities, like Atom or Eclipse, are pretty nifty and can save us a lot of time

## Automating Tasks Through Programming

### Benefits of Automation

* The benefits of automation for a bunch of activities like doing repetitive tasks, analyzing text, generating reports, and a lot more
* Look at automation like an IT force multiplier, a tool that can increase the effectiveness of an IT team without needing to increase the number of team members
	* In other words, automation can allow the IT infrastructure to scale, keeping pace with growth and demand
* **Benefits of Automation**
	1. __Scalability__ means that when more work is added to a system, the system can do whatever it needs to complete the work
		* For __example__, think about the impact on IT when a company hires a new employee
			* New employees might have to access a range of technology resources do their job
			* Onboarding task can include __creating__ a __user account__, a __mailbox__, and a __home folder__, and __setting up__ the appropriate __permissions__ to control access to various systems and resources
			* If the company doesn't hire a lot of employees over a given period, someone could manually do these tasks each time a new person is brought on board
			* But as the number of new employees increases, so does the time it takes to set them all up in the system
				* If a company hires 10 times its usual number of new employees in a week, the IT person in charge may find themselves performing nothing but a new employee account setup and going crazy at the same time
						<p align="center">
						  <a href="javascript:void(0)" rel="noopener">
							 <img width=600px  src="notesImages/manual_onboarding_sample_img_image21.png" alt="manual_onboarding_sample_img_image21"></a>
						</p>
			* They would probably have to put a bunch of other projects on hold until they've set up all the accounts
			* As a human, they may also make some mistakes during the provisioning process, like misspelling a name, forgetting a step, or giving a user count the wrong permissions
				* They then have to fix these mistakes, which means even more work
			* Basically, this (manually doing all the work mentioned above or manual onboarding) doesn't scale well in terms of financial resources, mental investment, or reliability, especially if the company continues to grow
			* **Automation of Onboarding**
				* Instead of having one person interact with each separate system to create a new user account, a mailbox, shared folder, and permissions, it'd be more efficient if the IT specialist could write a script to all of this
				* We could then have a computer do these tasks each time a new employee is hired
					* When given initial information, like the new employee's name and job function, this script could carry out each step automatically
				* So humans would only need to intervene if a task failed for some reason
				* The computer would execute each step in the script and in the given order in exactly the same way
				* It would never need to deviate from these instructions
			* **Improvement on Automation** mentioned above
				* Instead of having the IT specialist enter a new employees information into the script each time it's run, the script could just read the data from a company's human resources system
				* That will make the entire workflow begin automatically on the employees start date
		* In this example of automation, we've made a repetitive time-consuming task faster and more reliable
		* We've also freed up human resources allowing IT specialist to focus on more strategic or creative work
	1. __Centralizing Mistakes__
		* Which means if you find an error in a script, you can fix the error once and for all, which isn't the case for mistakes made by humans

> Automation is not a fix-all. If badly executed, automation can cause as many problems as it can solve


### Pitfalls of Automation

> __The Pareto Principle__ states that __20%__ of the __system administration tasks__ you perform are responsible for __80%__ of your __workload__. Therefore, identifying and automating those tasks will put your productivity through the roof!

* If automation is implemented without baffle design, it can cause some serious problems
* Any task or process we automate comes with a trade-off
	* Is the time and effort it'll take to write the script worth the potential automation benefits?
		* A simple heuristic that can help us decide is to estimate how long it takes us to do a certain task. And then multiply that by how many times we perform that task in a given time window
		* If we estimate that it would take less time to automate the tasks than it would to do it manually, chances are, it's a good candidate for automation
		* So, the time to write the automation is less than time to perform the task multiply by the amount of times you do it, then automate the task
						<p align="center">
						  <a href="javascript:void(0)" rel="noopener">
							 <img width=600px  src="notesImages/task_automation_formula_image22.png" alt="task_automation_formula_image22"></a>
						</p>
* Usually, the decision of whether to automate or not isn't so straightforward
* If a task is complex and performed in frequently, it may seem like automating is more trouble than it's worth
	* But keep in mind that once a task is wrapped in automation, anyone can do it
* It can be very useful to automate a complex error prone task
	* If it's critical that the tasks be done correctly, even if it's not executed that often
* A concept called the __Pareto Principle__ can also be a useful guideline to help you decide which tasks to automate
	* When applied to automation in IT, the __Pareto Principle__ states that 20% of the system administration tasks that you perform are responsible for 80% of your work
	* If you can identify and automate those 20% of your tasks, you could save yourself a whole lot of time
* It's tricky knowing when it's best to automate, an automation that's been implemented can be fragile
* If underlying systems change and the automation isn't updated accordingly, workflows can break
* __Bit-rot__ - The process of software failing out of step with the environment
	* For Example
		* Let's say the automatic backup program uses a disk identifier like `/dev/sda1` to know where the data to be saved is stored
		* What happens is the new disk is added to the server and disk identifier changes to `/dev/sdb1`
			* The automation will no longer be able to access this it thinks it should be backing up and it will fail
			* This process of software falling out of step with the environment is sometimes called __Bit-rot__
						<p align="center">
						  <a href="javascript:void(0)" rel="noopener">
							 <img width=600px  src="notesImages/bit_rot_example_image23.png" alt="bit_rot_example_image23"></a>
						</p>
	* The actual bits and script don't really decay it's the assumptions about the impulses signals the script relies on that rot
* A method of notification into your automated systems should be built that should notify human in case of error
	* This notification method could be
		1. an email
		1. a new entry in the internal issue tracker
		1. an update to a dashboard
		1. even a page to the person who's on call for the service
* The __system log__ can be an extremely useful source of information when your investigating an issue, we say that it's of forensic value
	* __Scripts__ can also be configured to __write__ to the __system log__, doing this creates an audit trail of useful troubleshooting information, which can help with the debugging process

### Practical Automation Example

* Some examples we can automate using Python
	* Say for example that you wanted to check the health of your computer
		* This can call for a lot of different checks like,
			1. verifying that there is enough disk space
			1. that the processor isn't an overloaded
			1. that it has the latest security updates
			1. that it's running services it's supposed to
		* To verify all of this, we need to know how to check each of these values
		* Of course, we'll do it by using some of the handy modules available to us
		* For example
			1. we can use a __shutil module__ and a __disk_usage function__ to check the current available disk space
							<p align="center">
							  <a href="javascript:void(0)" rel="noopener">
								 <img width=600px  src="notesImages/shutil_diskusage_example_image24.png" alt="shutil_diskusage_example_image24"></a>
							</p>
				* So we get the total number of bytes on disk, the amount that's used and the amount that's free
				* We can calculate the percentage of __free disk space__ by __dividing__ the __number of bytes free__ by __the total__ and __multiplying that by 100__
					```ruby
					>>> free_disk_percentage = number_free_bytes / total_bytes * 100
					```
					<p align="center">
					  <a href="javascript:void(0)" rel="noopener">
						 <img width=600px  src="notesImages/shutil_diskusage_freedisk_image25.png" alt="shutil_diskusage_freedisk_image25"></a>
					</p>
			1. To check cpu utilization
				* For this, we can use another module called __psutil__
					* This includes a **cpu_percent** function that returns a number showing how much of the CPU is being used
						* The amount of CPU used at each instant can change a lot, since processes are starting and finishing all the time
						* So this function receives an interval of seconds and returns an average percentage of usage in that interval
							```python
							>>> import psutil
							>>> psutil.cpu_percent(0.1)
							```
							<p align="center">
							  <a href="javascript:void(0)" rel="noopener">
								 <img width=600px  src="notesImages/psutil_cpupercent_example_image26.png" alt="psutil_cpupercent_example_image26"></a>
							</p>
* __Health Check Script__
	```python
	>>> #!/usr/bin/env python3
	>>> # script name: health_check.py
	>>> import shutil
	>>> import psutil
	>>>
	>>> def check_disk_usage(disk):
	>>> 	du = shutil.disk_usage(disk)
	>>> 	free = du.free / du.total * 100
	>>> 	return free > 20
	>>>
	>>> def check_cpu_usage():
	>>> 	usage = psutil.cpu_percent()
	>>> 	return usage < 75
	>>>
	>>>	if not check_disk_usage("/") or not check_cpu_usage():
	>>> 	print('Error')
	>>> else:
	>>> 	print("Everything is OK!")
	>>>
	```
	<p align="center">
	  <a href="javascript:void(0)" rel="noopener">
		 <img width=600px  src="notesImages/health_check_script_output_image27.png" alt="health_check_script_output_image27"></a>
	</p>
* __Extra Information__
	* A __virtual machine__, or __VM__ for short, is a computer simulated through software
		* This software simulates all the necessary hardware to the operating system that's running inside the machine
		* For some simulated hardware, the VM will use a portion of the underlying hardware for the simulation
			* For example
				* you're going to run eight different virtual machines on a single laptop, or even more, each with a portion of that disk space, memory, and CPU time
		* In other cases, it will simulate the hardware by talking to the operating system running on a physical machine
			* For example
				* a VM will use an emulated network card to communicate with the outside world
					* The networking packets going through that emulated card will be transmitted between the software that runs a VM and the operating system of the physical machine, which will then transmit the packets over the physical network
						<p align="center">
						  <a href="javascript:void(0)" rel="noopener">
							 <img width=600px  src="notesImages/vm_network_diagram_image28.png" alt="vm_network_diagram_image28"></a>
						</p>
	* Virtual Machines have become a staple in a lot of IT departments since they allow us to create new virtual computers on-demand
	* We can also reclaim the resources they use when they're no longer needed
		* If for example, you want to use software that's only available on one specific OS, it's easier to create a new virtual machine, uses software, and then delete the virtual machine once you're done

> A __virtual machine__, or __VM__, is a computer simulated through software. It simulates all the necessary hardware to the operating system that's running inside the machine.