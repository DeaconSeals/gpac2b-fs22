#################################
#	Environment Requirements	#
#################################

Your code must be written in Python 3 and function correctly in the base Conda environment running on a Linux OS. In a previous assignment, you were asked to create such an environment and it is what your submission with be graded and evaluated in.

If you've completed the environment setup assignment, you can activate the base conda environment with `conda activate base` if it is not already activated. Navigate to the directory of this repo. Start Jupyter using of the following commands
### WSL
`jupyter notebook --no-browser` then paste the generated link to your browser
### VM
`jupyter notebook` then the browser within the VM should automatically start with Jupyter running

#################################
#	Submission Rules	#
#################################

Included in your repository is a script named ”finalize.sh”, which you will use to indicate which version of your code is the one to be graded. When you are ready to submit your final version, run the command ./finalize.sh or ./finalize.sh -language_flag from your local Git directory, then commit and push your code. Running the finalize script without a language flag will cause the script to run an interactive prompt where you may enter your programming language. Alternatively, you can pass a -p flag when running the finalize script to indicate that you are submitting in Python 3 (i.e. `./finalize.sh -p`). The flag -j indicates Java, -cpp indicates C++, -cs indicates C#, and -p indicates Python 3. This script also has an interactive prompt where you will enter your Auburn username so the graders can identify you. The finalize script will create a text file, readyToSubmit.txt, that is populated with information in a known format for grading purposes. You may commit and push as much as you want, but your submission will be confirmed as ”final” if ”readyToSubmit.txt” exists and is populated with the text generated by ”finalize.sh” at 10:00pm on the due date. If you do not plan to submit before the deadline, then you should NOT run the ”finalize.sh” script until your final submission is ready. If you accidentally run ”finalize.sh” before you are ready to submit, do not commit or push your repo and delete ”readyToSubmit.txt.” Once your final submission is ready, run ”finalize.sh”, commit and push your code, and do not make any further changes to it

Late submissions will be penalized 5% for the first 24 hour period and an additional 10% for every 24 hour period thereafter.

If `finalize.sh` gives a permission error, try to run `chmod 755 finalize.sh` on the file to make it executable.

#################################
#	Git Cheat Sheet	#
#################################
* `git status` - view uncommited changes in local repo
* `git add *` - adds all un-ignored files to the staged commit
* `git commit -m "some message here"` - forms the commit with an in-line commit message
* `git push` - pushes your commit to your online repo