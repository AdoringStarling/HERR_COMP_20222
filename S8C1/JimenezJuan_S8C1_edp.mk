#JimenezJuan_S8C1_edp.mk

all:a.exe array.txt cuerda.PNG

cuerda.PNG : array.txt
	python JimenezJuan_S8C1_edp.py
	
array.txt : a.exe
	./a.exe
	
a.exe : JimenezJuan_S8C1_EDP.cpp
	g++ JimenezJuan_S8C1_EDP.cpp -o a.exe