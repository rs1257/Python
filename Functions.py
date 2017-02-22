
import os
import psutil
import shutil
import sys
import platform

import pylint
#import kivy
#import mixins

class FileMover(object):
	def __init__(self, src, des):
		self.src = src
		self.des = des

	def __enter__(self):
		shutil.move(self.src, self.des)

	def __exit__(self, exception_type, exception_value, traceback):
		shutil.move(self.des, self.src)

class FolderRenamer(object):

	def __init__(self, old, new):
		self.old = old
		self.new = new

	def __enter__(self):
		os.rename(self.old, self.new)

	def __exit__(self, exception_type, exception_value, traceback):
		os.rename(self.new, self.old)

def get_cpu_usage():
	cpupercentage = psutil.cpu_percent(1)
	return ("CPU Percentage: %s" %(cpupercentage))

def get_cpu_count():
	physicalcores = psutil.cpu_count(logical=False)
	logicalcores = psutil.cpu_count()
	return ("Physical Cores: %s, Logical Cores: %s" %(physicalcores, logicalcores))

def get_memory_info(): #doesnt look right
	memory = psutil.virtual_memory()
	total = memory[0]
	available = memory[1]
	used = memory[3]
	free = memory[4]
	return ("Total: %s, Available: %s, Used: %s, Free: %s" %(total, available, used, free))

def get_boot_time():
	return psutil.boot_time()

def main():
	
	src = r"C:\Users\destr\Desktop\1"
	des = r"C:\Users\destr\Desktop\2"
	#with FolderRenamer(src, des) as a:
	#	print ("Renaming")
	src2 = r"C:\Users\destr\Desktop\1\abc.txt"
	des2 = r"C:\Users\destr\Desktop\abc.txt"
	#with FileMover(src2, des2) as a:
	#	print ("Moving")	
	
	#while(1):
	#	pass
		#print (get_cpu_usage())	
		#print(get_cpu_count())
		#print (get_memory_info())
		#print (get_boot_time())
if __name__ == "__main__":
	for val in sys.argv:
		print (val)
	main()		
				