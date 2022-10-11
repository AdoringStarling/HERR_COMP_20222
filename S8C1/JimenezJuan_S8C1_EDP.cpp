#include <iostream>
#include <cmath>
#include <cstdlib>
#include <time.h>
#include <vector>
#include <bits/stdc++.h>
#include <fstream>
#include <stdio.h>


using namespace std;

//https://stackoverflow.com/questions/47871245/saving-matrix-to-a-file-txt-format-in-cghgh

int main(){
    double c=300.0;
    double L=2.0;
    double h=0.1;
    double dx=0.02;
    int size=100;
    double dt=0.5*(dx/c);
    double u_pas[size]={};//u pasado sigue ecuacion de la recta__
    double u_pre[size]={};//u presente u1_i
    double u_fut[size]={};//u presente u(j+1)_i
    //u pasado
    for (int i = 0; i < size; i++){
        if (i<=50){
            u_pas[i]=(((0.1)*(dx*i))+0.0);
                    }
        else{
            u_pas[i]=(((-0.1)*(dx*i))+0.2);
                    };
                        };
    //u presente
     for (int i = 1; i < size; i++){
            u_pre[i]=u_pas[i]+(0.5*(((c*c)*(dt*dt))/(dx*dx)))*(u_pas[i+1]-(2*(u_pas[i]))+u_pas[i-1]);};
	u_pre[0]=0;//condiciones de frontera
    //u futuro
     for (int i = 1; i < size; i++){
            u_fut[i]=(2*u_pre[i])-(u_pas[i])+(((c*c)*(dt*dt))/(dx*dx))*(u_pre[i+1]-(2*(u_pre[i]))+u_pre[i-1]);};
	u_fut[0]=0;//condiciones de frontera
	ofstream myfile;
	myfile.open ("array.txt");
	for (int i = 0; i < size; i++){
		myfile <<u_pas[i];
		myfile << ";";}
	myfile << "\n";
	for (int i = 0; i < size; i++){
		myfile <<u_pre[i];
		myfile << ";";}
	myfile << "\n";
	 for (int t = 3; t < 500; t++){
			for (int i = 0; i < size; i++){
				u_pas[i]=u_pre[i];
				u_pre[i]=u_fut[i];}
			u_pas[0]=0; //condiciones de frontera
			u_pre[0]=0; //bis
			for (int i = 0; i < size; i++){
				u_fut[i]=(2*u_pre[i])-(u_pas[i])+(((c*c)*(dt*dt))/(dx*dx))*(u_pre[i+1]-(2*(u_pre[i]))+u_pre[i-1]);
				myfile <<u_fut[i];
				myfile << ";";}
		 myfile << "\n";
				};
	myfile.close();
    }