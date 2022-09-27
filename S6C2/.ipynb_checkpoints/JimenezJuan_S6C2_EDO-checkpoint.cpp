#include <iostream>
#include <cmath>
#include <cstdlib>
#include <time.h>
#include <vector>
#include <bits/stdc++.h>
#include <fstream>


using namespace std;


double func(double tn,double yn) {
    return -1*(yn);
}

double Exponentiation(double x)
{
    double result = exp(-x);
    return result;
}

int main(){
	double t1=0;
	double t2=300;
	double h=0.1;
	int size=(t2-t1)/h;
    double y1[size] = {};
	double y2[size] = {};
	double y3[size] = {};
	double x1[size] = {};
	y1[0]=1;
	double tm=0;
	//Euler
    for (int i = 1; i < size; i++){
		tm=0.1+tm;
        y1[i]=y1[i-1]+(h*func(tm,y1[i-1]));
		x1[i]=tm;};
	tm=00;
	//Runge Kutta
    for (int i = 1; i < size; i++){
		tm=0.1+tm;
		double k1=(h*func(tm,y1[i-1]));
		double k2=(h*func(tm+(h/2),y1[i-1]+(k1/2)));
		double k3=h*func(tm+(h/2),y1[i-1]+(k2/2));
		double k4=(h*func(tm+h,y1[i-1]+k3));
        y3[i]=y1[i-1]+((1/6)*(k1+(2*k2)+(2*k3)+k4));
		x1[i]=tm;};
	//_______
    for (int i = 0; i < size; i++){
        y2[i]= exp(-x1[i]);};
    ofstream myfile ("y1.txt");
    if (myfile.is_open())
    {
		for(int count = 0; count < size; count ++){
            myfile << y1[count] << " " ;
    }
		myfile.close();
      };
    ofstream myfile2 ("y2.txt");
    if (myfile2.is_open())
    {
		for(int count = 0; count < size; count ++){
            myfile2 << y2[count] << " " ;
    }
		myfile2.close();
      };
    ofstream myfile3 ("y3.txt");
    if (myfile3.is_open())
    {
		for(int count = 0; count < size; count ++){
            myfile3 << y3[count] << " " ;
    }
		myfile3.close();
      };
    ofstream myfile1 ("x1.txt");
    if (myfile1.is_open())
    {
		for(int count = 0; count < size; count ++){
            myfile1 << x1[count] << " " ;
    }
		myfile1.close();
      };
    return 0;
    }
    
