#include <iostream>
#include <cmath>
#include <cstdlib>
#include <time.h>
#include <vector>
#include <bits/stdc++.h>
#include <fstream>
#include <stdio.h>


using namespace std;

int main(){
    double v=0.0004;
    double dx=1;
    int size=100;
    double dt=100;// Mas o menos 125
	double t_temp[size][size]={};
	ofstream f0;
	f0.open ("t0.txt");
    //t init
    for (int f = 0; f < size; f++){
		for (int c = 0; c < size; c++){
			if (f>20 && f<=40 && c>40 && c<=60){
				t_temp[f][c]=100;
				f0<<t_temp[f][c];
						}
			//if (f=0){
			//	t_temp[f][c]=0;
			//	f0<<t_temp[f][c];
			//			}
			else{
				t_temp[f][c]=50;
				f0<<t_temp[f][c];
				}
			f0 << ";";
		};
		f0 << "\n";};
	//t pos	
	for (int t = 1; t < 25+1; t++){
		for (int f = 0; f < size; f++){
			for (int c = 0; c < size; c++){
						if (f==0 or f==99 or c==0 or c==99){
											t_temp[f][c]=50;
											//f0<<t_temp[f][c];
											//f0 << ";";
													}
						else {
							t_temp[f][c]=(dt*(v*(((t_temp[f+1][c]-(2*t_temp[f][c])+t_temp[f-1][c])/(dx*dx))+((t_temp[f][c+1]-(2*t_temp[f][c])+t_temp[f][c-1])/(dx*dx)))))+t_temp[f][c];	
								}
						if (t==1 or t==10 or t==25){
											f0<<t_temp[f][c];
											f0 << ";";
													}
						
											}
	
			if (t==1 or t==10 or t==25){
								f0 << "\n";};
										}
									}	
	f0.close();
			}