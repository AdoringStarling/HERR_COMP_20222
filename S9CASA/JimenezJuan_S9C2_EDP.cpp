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
    double L=100;
    double dx=1;
    int size=100;
    double dt=0.5*((dx*dx)/v);
	double t_temp[size][size+1]={};
	ofstream f0;
	f0.open ("t0.txt");
    //t init
    for (int c = 0; c < size; c++){
		for (int f = 0; f < size; f++){
			if (c=0){
				f0<<0;
				f0 << ";";
			}
			else if (f>20 && f<=40 && c>40 && c<=60){
				t_temp[f][c]=100;
				f0<<t_temp[f][c];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
				f0 << ";";
						}
			else{
				t_temp[f][c]=50;
				f0<<t_temp[f][c];
				f0 << ";";
				}}
		f0 << "\n";};
	f0.close();
	//t pos	
	for (int t = 1; t < 100; t++){
		for (int f = 1; f < size-1; f++){
			for (int c = 1; c < size-1; c++){
						t_temp[f][c]=(dt*(v*(((t_temp[f+1][c]-(2*t_temp[f][c])+t_temp[f-1][c])/(dx*dx))+((t_temp[f][c+1]-(2*t_temp[f][c])+t_temp[f][c-1])/(dx*dx)))))+t_temp[f][c];
    }};}}