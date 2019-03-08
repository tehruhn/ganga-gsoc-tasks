import os

job = Job()
job.application = Executable()
job.application.exe = File("count-word.sh")
args = [["page0.pdf"],["page1.pdf"],["page2.pdf"],["page3.pdf"],["page4.pdf"],["page5.pdf"],["page6.pdf"],["page7.pdf"],["page8.pdf"],["page9.pdf"],["page10.pdf"],["page11.pdf"]]
splitter = ArgSplitter(args=args)
filelist = []
for i in range(len(args)):
	filename = args[i][0]
	filelist.append(filename)
job.application.args = filelist
job.splitter = splitter
job.inputfiles = filelist
job.backend = "Local"
job.postprocessors = CustomMerger(module="./custommerge.py")
job.submit()