#JimenezJuan_S6C2.mk
    
all: EULER.png

EULER.png : PLOTS_JuanJimenez_S6C2.py x1.txt y1.txt y2.txt y3.txt
	python PLOTS_JuanJimenez_S6C2.py
    
x1.txt : a.exe
	./a.exe

y1.txt : a.exe
	./a.exe

y2.txt : a.exe
	./a.exe

y3.txt : a.exe
	./a.exe
	
a.exe : JimenezJuan_S6C2_EDO.cpp
	g++ JimenezJuan_S6C2_EDO.cpp -o a.exe