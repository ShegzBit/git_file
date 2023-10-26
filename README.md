# A GIT UTITLITY
## git\_file

This repo contains a `git_file` utility that can be used to clone single files from a repo

### This Utility Can Come In Handy For
* Selective Download: When you only need a specific file or subset of files from a large repository, cloning the entire repository can be time-consuming and unnecessary. A utility that allows for single file cloning can save time and bandwidth.

* Limited Storage: If you’re working on a device with limited storage, cloning an entire repository might not be feasible. Being able to clone only the necessary files can help manage storage constraints.

* Confidentiality: In cases where a repository contains sensitive or confidential information in some files, being able to clone only non-sensitive files can help maintain security and confidentiality.

* Efficiency: If you’re working in a team and different team members are responsible for different files, being able to clone only the files relevant to your part of the project can make the workflow more efficient.

* Learning and Teaching: If you’re using GitHub for educational purposes, such as learning or teaching coding, being able to clone individual files can make it easier to focus on specific lessons or exercises.

* Modular Projects: For modular projects where different parts of the codebase are loosely coupled and can function independently, cloning only the necessary modules/files can be more practical.

### How To Install
* Clone this repo locally on your sytem
* enter the directory
* run the configuration file
* leave the directory and source bashrc
* You're ready to use _git_file_
#### More Detailed Instruction
* First run this to clone the repo
`git clone https://github.com/ShegzBit/git_file`
* Enter the directory
`cd git_file`
* Run configuration file
`./configuration.sh`
leave the directory
`cd ..`
source your bashrc file
`source ~/.bashrc`
*__Now You're ready to use git_file utility__*

#### Installation Code Block
```
git clone https://github.com/ShegzBit/git_file
cd git_file
./configuration.sh
cd ..
source ~/.bashrc
```

### How to use
* Navigate to the repo you which to clone
* Click on the file and copy the link
then run `git_file <file url>`
*Sample*
![link img] (./'link img')
`git_file https://github.com/ShegzBit/alx-higher_level_programming/blob/main/0x0E-SQL_more_queries/101-avg_temperatures.sql`
and the file will be added
![dir img](./'dir img')

### Options and Features
#### -r Option
`-r <new_file name>`
* Renames the file to the name specified after it
* If not specified the file name from the repo is used
*-r not specified*
!dir img

*-r specified*

![git\_file -r](/home/shegz/git_file/'git_file -r.png')

#### -t Option
`-t`
* truncates a file if it already exists and write new content to it
* if not specified and the file already exists the program preserves the file and fails saying truncate option not passed
![git\_file -t](./'git_file -t')

Thanks for using my utility feel free to suggest new features and I'll look into it when I'm free
You can conect with me on
Linkedin: [Feranmi Awotubo](https://www.linkedin.com/in/feranmi-awotubo-a2ba2b263/)
Twitter: [Feranmi Awotubo](https://twitter.com/feranmiawotubo1)
Telegram: [Feranmi Awotubo](t.me/+2347089043898)
