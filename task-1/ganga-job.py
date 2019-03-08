# SOLUTION TO TASK 1B
# GSoC 2019
# AUTHOR - TARUN RAHEJA

import os

#starts new job
job = Job()
#specifies executable to run on Grid
job.application = Executable()
job.application.exe = File("count-word.sh")
#specifies pagewise arguments to the executable
args = [["page0.pdf"],["page1.pdf"],["page2.pdf"],["page3.pdf"],["page4.pdf"],["page5.pdf"],["page6.pdf"],["page7.pdf"],["page8.pdf"],["page9.pdf"],["page10.pdf"],["page11.pdf"]]
#splits the job
splitter = ArgSplitter(args=args)
#creates list of file names
filelist = []
for i in range(len(args)):
	filename = args[i][0]
	filelist.append(filename)
#assigns filelist to job applicatio arguments
job.application.args = filelist
#assigns splitter to job application
job.splitter = splitter
#assigns filelist to inputfiles
job.inputfiles = filelist
#specifies backend
job.backend = "Local"
#specifier custom merger
job.postprocessors = CustomMerger(module="./custommerge.py")
job.submit()