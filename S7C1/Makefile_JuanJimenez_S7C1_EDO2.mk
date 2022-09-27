#JimenezJuan_S7C1.mk
    
all: EULER_1.png yeux.txt yeuv.txt xeu.txt a.exe

EULER_1.png : PLOTS_JUanJimenez_S7C1_EDO2.py yeux.txt yeuv.txt xeu.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py
    
yeux.txt : a.exe
	./a.exe

yeuv.txt : a.exe
	./a.exe

xeu.txt : a.exe
	./a.exe
	
a.exe : JuanJimenez_S7C1_EDO2.cpp
	g++ JuanJimenez_S7C1_EDO2.cpp -o a.exe