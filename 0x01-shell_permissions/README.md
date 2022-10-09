# SHELL PERMISSIONS

This project has 18 files that contains scripts of different shell permission tasks.

The files and the tasks are given below:

**0-iam_betty** -- contains script that switches the current user to the user betty using exactly 8 characters in the command.

**1-who_am_i** -- contains a script that prints the effective username of the current user.

**2-groups** -- contains a script that prints all the groups the current user is part of.

**3-new_owner** -- contains a script that changes the owner of the file hello to the user betty.

**4-empty** -- contains a script that creates an empty file called hello.

**5-execute** -- contains a script that adds execute permission to the owner of the file hello that is in the working directory.

**6-multiple_permissions** -- contains a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello in the directory.

**7-everybody** -- contains a script without commas that adds execution permission to the owner, the group owner and the other users, to the file hello in the durectory.

**8-James_Bond** -- contains a script without commas that sets the permission to the file hello in the directory as follows:

-Owner: no permission at all.
-Group: no permission at all.
-Other users: all the permissions.

**9-John_Doe** -- contains a script without commas that sets the mode of the file hello in the dirctory to this:
```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```

**10-mirror_permissions** -- contains a script that sets the mode of the file hello the same as olleh’s mode with both files in the working directory.

**11-directories_permissions** -- contains a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files will not changed.

**12-directory_permissions** -- contains a script that creates a directory called my_dir with permissions 751 in the working directory.

**13-change_group** -- contains a script that changes the group owner to school for the file hello in the working directory.

**100-change_owner_and_group** -- contains a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

**101-symbolic_link_permissions** -- contains a script that changes the owner and the group owner of _hello to vincent and staff respectivelyy with
-The file _hello in the working directory and a symbolic link.

**102-if_only** -- contains a script that changes the owner of the file hello to betty only if it is owned by the user guillaume. Hello is in the working directory.

**103-Star_Wars** -- contains a script that will play the StarWars IV episode in the terminal.
