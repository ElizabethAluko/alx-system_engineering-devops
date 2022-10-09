# SHELL BASICS

This project contains 20 files that give the shell commands of some tasks.

The files and the tasks are:

**0-current_working_directory** -- contains a script that prints the absolute path name of the current working directory.

**1-listit** -- contains script that display the contents list of your current directory.

**2-bring_me_home** -- contains script that changes the working directory to the user's home directory.

**3-listfiles** -- contains script that display current directory contents in a long format.

**4-listmorefiles** -- contains script that display current directory contents, including hidden files(starting with .) in long format.

**5-listfilesdigitonly** -- contains script that display current directory contents in long format with user and group IDs displayed numerically and hidden files (starting with .)

**6-firstdirectory** -- contains script that creates a directory named my_first_directory in the /tmp/directory

**7-movethatfile** -- contains script that move the file betty from /tmp/ to /tmp/my_first_directory.

**8-firstdelete** -- contains script that delete the file betty.

**9-firstdirdeletion** -- contains script that delete the directory my_first_directory that is in the /tmp directory.

**10-back** -- contains script that changes the working directory to the previous one.

**11-lists** -- contains script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

**12-file_type** -- contains script that prints the type of the file named iamafile.

**13-symbolic_link** -- contains script that create a symbolic link to /bin/ls, named __ls__. The symbolic link will be created in the current working directory.

**14-copy_html** -- contains a script that create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

**100-lets_move** -- contains script that moves all files beginning with an uppercase letter to an existing directory /tmp/u.

**101-clean_emacs** -- contains script that deletes all files in the current working directory that end with the character ~.

**102-tree** -- contains script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory using only two spaces in the script.

**103-commas** -- contains script that lists all the files and directories of the current directory, separated by commas (,) also with the following conditions:

-Directory names should end with a slash (/)
-Files and directories starting with a dot (.) should be listed
-The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
-Only digits and letters are used to sort; Digits should come first
-Assume that all the files we will test with will have at least one letter or one digit
-The listing should end with a new line.

**school.mgc** -- magic script that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.

