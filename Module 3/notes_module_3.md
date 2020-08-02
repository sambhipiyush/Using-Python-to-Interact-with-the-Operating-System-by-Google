Using Python to Interact with the Operating System
==================================================

by Google

# Module 3
#
## Title: Regular Expressions

## Regular Expressions

### What are regular expressions?

* __Regular Expression__
	* A regular expression, also known as __regex__ or __regexp__, is essentially a search query for text that's expressed by __string pattern__
	* When you run a search against a particular piece of text, anything that matches a regular expression pattern you specified, is returned as a result of the search
	* Regular expressions let you answer the questions like
		1. what are all the four-letter words in a file?
		1. how many different error types are there in this error log?
	* In other words, __regular expressions__ allow us to search a text for strings matching a specific pattern
	* Knowing about regular expressions can be useful for anyone who needs to perform text processing
	* For example
		* If there is a file that lists NFS mounts and options and there is a need to pull only the server name, we can write a regular expression that strips each line of the excess data and returns only a list of the information that is needed
* We can also use command line tools that know how to apply regexs, like __grep__, __sed__, or __awk__
* We can even use regular expressions inside text processing tools like code or document __editors__

### Why use regular expressions?

* For example, let's say we have log entries with a typical log line format like the shown in image below
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/log_entry_example_image1.png" alt="log_entry_example_image1"></a>
			</p>
	* We want to extract the process identifier from this line, which is a number between the square brackets 12345
	* There's a lot of extra text in this log line that we don't need, like the date, the computer name and other info
	* We could extract the process ID by using the index method to find the first square bracket in the string
		* Remember that when accessing strings, the index of the character is the position of that character in the string starting from 0
	* In this example, the index of the first square bracket would be 39
		* If we don't want to capture the square brackets, we will start at the next version and include five more characters after that
			```python
			>>> log = "July 31 07:51:48 .... [12345] ..... upgrade" # complete text in image above
			>>> index = log.index('[')
			>>> print(log[index+1:index+6])
				12345
			```
		* Although we get the text that we wanted, we might hit a few bumps down the road
			* One problem is we don't know for sure how long the process ID string will be in all cases
			* In this example, we can see that it's five characters long. But that may change in the future if the computers restarted, or the number of processes increases
			* This could also break if for any reason, the line includes another square bracket before the process ID
			* So it's a solution but it's a very brittle one
	* We can also use regular expression to solve this problem and to extract the process ID in a more robust fashion
		* For that, we're going to import the __re module__, which lets us use the __search()__ function to find regular expressions inside strings
			```python
			>>> import re
			>>> log = "July 31 07:51:48 .... [12345] ..... upgrade" # complete text in image above
			>>> regex = r'\[(\d+)\]'
			>>> result = re.search(regex, log)
			>>> print(result[1])
				12345
			```
		* this regular expression will work no matter where our process ID shows up or how long or short the line is
		* As long as there's a single sequence of numbers in the string marked by square brackets, this regex will extract those numbers for us

### Basic Matching with grep

* We can also use regular expressions with a bunch of command line tools
* Grep is an especially easy to use yet extremely powerful tool for applying regexes
	* It's a great way to easily try out some expressions and get familiar with them
* __Remember__, that grep works by printing out any line that matches the query that we pass it
	* So for a simplest query of passing a plain old string, grep will print any lines containing that string in the file that we give it
* Example
	* Let's try this out using grep to find words inside the `/usr/share/dict/words` file, which is a file that some spell-checking programs use to verify if the word exists or not
	* This file contains one word per line
	* We'll start by looking at words that contain the particle __thon__
		```shell
		>>> grep thon /usr/share/dict/words
		```
		<p align="center">
		  <a href="javascript:void(0)" rel="noopener">
			 <img width=600px  src="notesImages/grep_thon_dict_words_image2.png" alt="grep_thon_dict_words_image2"></a>
		</p>
	* So when we call grep with thon as a pattern to match on and we pass our list of words as a file, we see that it matches with a bunch of different words
		* These words, all contain the string thon somewhere inside of them, which is why they appear in our results
	* We also see that the output is highlighted for us, showing us the matching part of the line in a different color
		* This added visual indicator is something that grep does for us so that we can easily see where the match occurred
	* It's worth calling out that the string we're passing in __grep__ is __case sensitive__
	* If we wanted to match a string regardless of case, we will have to pass the `-i` parameter to the __grep__ command
		```shell
		>>> grep -i python /usr/share/dict/words
		```
		<p align="center">
		  <a href="javascript:void(0)" rel="noopener">
			 <img width=600px  src="notesImages/grep_python_i_dict_words_image3.png" alt="grep_python_i_dict_words_image3"></a>
		</p>
	* So we now know that any basic string is already a regular expression which will match a line that contains that string
* a __dot__ matches any character
	* This means that if we include a __dot__ in our expression, that __dot__ is a __wildcard__ that can be replaced by any other character in the results
			```shell
			>>> grep l.rts /usr/share/dict/words
			```
			<p align="center">
			  <a href="javascript:void(0)" rel="noopener">
				 <img width=600px  src="notesImages/grep_pattern_dot_image4.png" alt="grep_pattern_dot_image4"></a>
			</p>
		* This pattern matches three different words; alerts, blurts, and flirts
		* Check out how for each of those words, the dot in our pattern was substituted by different letter
* We can find portions of texts that match a given pattern even when the pattern isn't a whole word
* For Example, We could use these
	1. to look for entries in a log file that match a certain format
	1. to find rows in a CSV file that share the same characteristics even if they are not exactly the same
* Some characters that we can use in Regular Expression are
	1. caret or circumflex or ^
		* The circumflex indicates the beginning
	1. dollar sign or $
		* The dollar sign indicates the end of the line
* For example
	1. to look for all the words that start with a string fruit, we would write grep circumflex fruit in our file
		```shell
		>>> grep ^fruit /usr/share/dict/words
		```
		<p align="center">
		  <a href="javascript:void(0)" rel="noopener">
			 <img width=600px  src="notesImages/grep_pattern_caret_image5.png" alt="grep_pattern_caret_image5"></a>
		</p>
	1. to look for all the words that end with a string cat, we would write grep cat dollar sign in our file
		```shell
		>>> grep cat$ /usr/share/dict/words
		```
		<p align="center">
		  <a href="javascript:void(0)" rel="noopener">
			 <img width=600px  src="notesImages/grep_pattern_dollar_image6.png" alt="grep_pattern_dollar_image6"></a>
		</p>
* __Remember__ is that the circumflex and the dollar sign specifically match the start and end of the line, not a string

## Basic Regular Expressions

### Simple Matching in Python

* 

## Advanced Regular Expressions

### S