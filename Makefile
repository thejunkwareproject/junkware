# Junkware Makefile
#~~~~~~~~~~~~
# Everything you ever need to junkify your own DNA
# 


download_data:
	@(cd data/molecules; sh dl_molecules.sh )

test:
	nosetests

run: 
	@(cd app; python app.py)
