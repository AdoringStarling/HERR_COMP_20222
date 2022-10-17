#Makefile_JimenezJuan_S9C2_EDP.mk

all:a.exe t0.txt diff.png

diff.png : t0.txt
	python PLOTS_JimenezJuan_S9C2_EDP.py
	
t0.txt : a.exe
	./a.exe
	
a.exe : JimenezJuan_S9C2_EDP.cpp
	g++ JimenezJuan_S9C2_EDP.cpp -o a.exe