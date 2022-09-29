#JimenezJuan_S7C1.mk
    
all: Euler.PNG  Runge_Kutta.PNG Euler_a.PNG  Runge_Kutta_a.PNG Leap_Frog.PNG yeux.txt yeuv.txt xeu.txt a.exe aa.exe yrkv.txt yrkx.txt ylfv.txt ylfx.txt xlfv.txt xlfx.txt yeuxa.txt yeuva.txt xeua.txt yrkva.txt yrkxa.txt

Euler_a.PNG : PLOTS_JUanJimenez_S7C1_EDO2.py yeuxa.txt yeuva.txt xeua.txt yeux.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py
	
Runge_Kutta_a.PNG : PLOTS_JUanJimenez_S7C1_EDO2.py yrkva.txt yrkxa.txt xeua.txt yeux.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py

Leap_Frog.PNG : PLOTS_JUanJimenez_S7C1_EDO2.py yeux.txt yeuv.txt xeu.txt yrkv.txt yrkx.txt ylfv.txt ylfx.txt xlfv.txt xlfx.txt yeuxa.txt yeuva.txt xeua.txt yrkva.txt yrkxa.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py

Runge_Kutta.PNG : PLOTS_JUanJimenez_S7C1_EDO2.py yeux.txt yeuv.txt xeu.txt yrkv.txt yrkx.txt ylfv.txt ylfx.txt xlfx.txt xlfv.txt yeuxa.txt yeuva.txt xeua.txt yrkva.txt yrkxa.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py
	
Euler.PNG : PLOTS_JUanJimenez_S7C1_EDO2.py yeux.txt yeuv.txt xeu.txt yrkv.txt yrkx.txt ylfv.txt ylfx.txt xlfv.txt xlfx.txt yeuxa.txt yeuva.txt xeua.txt yrkva.txt yrkxa.txt
	python PLOTS_JUanJimenez_S7C1_EDO2.py

yeuxa.txt : aa.exe
	./aa.exe
yeuva.txt : aa.exe
	./aa.exe
xeua.txt : aa.exe
	./aa.exe
yrkxa.txt: aa.exe
	./aa.exe
yrkva.txt: aa.exe
	./aa.exe
	
xlfv.txt : a.exe
	./a.exe

xlfx.txt : a.exe
	./a.exe
	
ylfv.txt : a.exe
	./a.exe

ylfx.txt : a.exe
	./a.exe

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

aa.exe : JuanJimenez_S7C1_EDO2.cpp
	g++ JuanJimenez_S7C1_EDO2-ammor.cpp -o aa.exe
	
a.exe : JuanJimenez_S7C1_EDO2.cpp
	g++ JuanJimenez_S7C1_EDO2.cpp -o a.exe