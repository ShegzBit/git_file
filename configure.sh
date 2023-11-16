#!/usr/bin/env bash

which python > /dev/null 2>&1
if [ $? -ne 0 ]
then
	sudo apt-get install python3
	if [ $? -ne 0 ]; then
		echo 'Failed to install python'
	else
		pip3 install requests
		if [ $? -ne 0 ]; then
			echo 'Failed to install requests'
		fi
	fi
else
	pip show requests > /dev/null 2>&1
	if [ $? -ne 0 ]; then
		 pip3 install requests
                	if [ $? -ne 0 ]; then
                        	echo 'Failed to install requests'
	                fi
	fi
fi
	
mv ../git_file ../.git_file
cd ../.git_file

dir=$(pwd)
py_get=$dir"/.py_get"
program=$dir"/.new_run"

chmod 755 .py_get

git_alias="git_file()\n {\n"$program" "\$@"\n}"

py_get_alias="get_file_from_github_using_python_request()\n {\n"$py_get" "\$@"\n}"

echo -e "$git_alias" >> ~/.bashrc

# set up new_run

echo '#!/usr/bin/env bash' > .new_run
echo -e $py_get_alias >> .new_run
cat .run.sh >> .new_run
chmod 755 .new_run

mv configure.sh .configure.sh
