#JimenezJuan_S6CC1.mk
    
all: aleatorios.png aleatorios_con_impares.png
    
aleatorios.png : JimenezJuan_S6CC1.py example1.txt
    python JimenezJuan_S6CC1.py
    
aleatorios_con_impares.png : JimenezJuan_S6CC1.py example2.txt
    python JimenezJuan_S6CC1.py