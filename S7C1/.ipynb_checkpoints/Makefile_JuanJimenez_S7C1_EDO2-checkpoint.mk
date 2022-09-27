#JimenezJuan_S7C1.mk
    
all: EULER_1.png Runge_Kutta_1.PNG yeux.txt yeuv.txt xeu.txt a.exe yrkv.txt yrkx.txt

Runge_Kutta_1.PNG : PLOTS_JUanJimenez_S7C1_EDO2.py yeux.txt yeuv.txt xeu.txt yrkv.txt yrkx.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py
	
EULER_1.png : PLOTS_JUanJimenez_S7C1_EDO2.py yeux.txt yeuv.txt xeu.txt yrkv.txt yrkx.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py


yrkv.txt : a.exe
	./a.exe

yrkx.txt : a.exe
	./a.exe
	
yeux.txt : a.exe
	./a.exe

yeuv.txt : a.exe
	./a.exe

xeu.txt : a.exe
	./a.exe
	
a.exe : JuanJimenez_S7C1_EDO2.cpp
	g++ JuanJimenez_S7C1_EDO2.cpp -o a.exe