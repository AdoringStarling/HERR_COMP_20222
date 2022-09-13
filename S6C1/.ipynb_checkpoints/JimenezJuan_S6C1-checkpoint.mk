#JimenezJuan_S6CC1.mk
    
all: aleatorios.png aleatorios_con_impares.png example1.txt example2.txt JimenezJuan_S6C1.exe

aleatorios.png : JimenezJuan_S6C1.py example1.txt
	python JimenezJuan_S6C1.py
    
aleatorios_con_impares.png : JimenezJuan_S6C1.py example2.txt
	python JimenezJuan_S6C1.py

example1.txt : JimenezJuan_S6C1.exe
	./JimenezJuan_S6C1.exe

example2.txt : JimenezJuan_S6C1.exe
	./JimenezJuan_S6C1.exe

JimenezJuan_S6C1.exe : JimenezJuan_S6C1.cpp
	g++ JimenezJuan_S6C1.cpp -o JimenezJuan_S6C1.exe