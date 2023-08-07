import site,os,sys,__main__

def add_parent_pth(fn):
	stop=False
	while not stop:
		check_for=os.path.join(fn,".pth")
		if os.path.exists(check_for):
			#print("found: ",fn)
			site.addsitedir(fn)
			stop=True

		else:
			if fn==os.path.dirname(fn):
				stop=True

			fn=os.path.dirname(fn)

add_parent_pth(sys.argv[0])
add_parent_pth(os.getcwd())
if hasattr(__main__,"__file__"):
	add_parent_pth(__main__.__file__)
