#include <iostream>
#include <cmath>
#include <cstdlib>
#include <time.h>
#include <vector>
#include <bits/stdc++.h>
#include <fstream>


using namespace std;

double funcv(double yeux) {
	double k=50; //N/M
	double m=0.2; //kg
    return -(k/m)*yeux;
}

double Exponentiation(double x)
{
    double result = exp(-x);
    return result;
}

int main(){
	double t1=0;
	double t2=10;
	double h=0.01;
	int size=(t2-t1)/h;
    double yeux[size] = {};
	double yeuv[size] = {};
	double xeu[size] = {};
	yeux[0]=0.1;
	yeuv[0]=0;
	double tm=0;
	//Euler
    for (int i = 1; i < size; i++){
		tm=0.1+tm;
        yeuv[i]=yeuv[i-1]+(h*funcv(yeux[i-1]));
		yeux[i]=yeux[i-1]+(h*yeuv[i]);
		xeu[i]=tm;};
    ofstream myfile ("yeux.txt");
    if (myfile.is_open())
    {
		for(int count = 0; count < size; count ++){
            myfile << yeux[count] << " " ;
    }
		myfile.close();
      };
    ofstream myfile2 ("yeuv.txt");
    if (myfile2.is_open())
    {
		for(int count = 0; count < size; count ++){
            myfile2 << yeuv[count] << " " ;
    }
		myfile2.close();
      };
    ofstream myfile3 ("xeu.txt");
    if (myfile3.is_open())
    {
		for(int count = 0; count < size; count ++){
            myfile3 << xeu[count] << " " ;
    }
		myfile3.close();
      };
	//Runge Kutta
    double yrkx[size] = {};
	double yrkv[size] = {};
	yrkx[0]=0.1;
	yrkv[0]=0;
    for (int i = 1; i < size; i++){
		double k1x=h*(yrkv[i-1]);
		double k1v=h*funcv(yrkx[i-1]);
		double k2x=h*(yrkv[i-1]+(k1v/2));
		double k2v=h*funcv(yrkx[i-1]+(k1x/2));
		double k3x=h*(yrkv[i-1]+(k2v/2));
		double k3v=h*funcv(yrkx[i-1]+(k2x/2));
		double k4x=h*(yrkv[i-1]+k3v);
		double k4v=h*funcv(yrkx[i-1]+k3x);
		yrkx[i]=yrkx[i-1]+((1.0/6)*(k1x+(2*k2x)+(2*k3x)+k4x));
		yrkv[i]=yrkv[i-1]+((1.0/6)*(k1v+(2*k2v)+(2*k3v)+k4v));
		};
    ofstream yrkxf ("yrkx.txt");
    if (yrkxf.is_open())
    {
		for(int count = 0; count < size; count ++){
            yrkxf << yrkx[count] << " " ;
    }
		yrkxf.close();
      };
    ofstream yrkv1 ("yrkv.txt");
    if (yrkv1.is_open())
    {
		for(int count = 0; count < size; count ++){
            yrkv1 << yrkv[count] << " " ;
    }
		yrkv1.close();
      };
	//leap frog
	int sizelf=(t2-t1)/h;
	double ylfx[size] = {};
	double ylfv[size] = {};
	double xlfx[size] = {};
	double xlfv[size] = {};
	ylfx[0]=0.1;
	//ylfv[0]=0;
	xlfx[0]=0.01;
	xlfv[0]=0.01/2;
	ylfv[0]=(0.5*(h*funcv(ylfx[0])));					 
    for (int i = 1; i < size; i++){
		ylfx[i]=ylfx[i-1]+(h*(ylfv[i-1]));
		ylfv[i]=ylfv[i-1]+(h*funcv(ylfx[i]));
		xlfx[i]=xlfx[i-1]+h;
		xlfv[i]=xlfv[i-1]+h;
		};
    ofstream ylfx1 ("ylfx.txt");
    if (ylfx1.is_open())
    {
		for(int count = 0; count < size; count ++){
            ylfx1 << ylfx[count] << " " ;
    }
		ylfx1.close();
      };
    ofstream ylfv1 ("ylfv.txt");
    if (ylfv1.is_open())
    {
		for(int count = 0; count < size; count ++){
            ylfv1 << ylfv[count] << " " ;
    }
		ylfv1.close();
      };
    ofstream xlfx1 ("xlfx.txt");
    if (xlfx1.is_open())
    {
		for(int count = 0; count < size; count ++){
            xlfx1 << xlfx[count] << " " ;
    }
		xlfx1.close();
      };
    ofstream xlfv1 ("xlfv.txt");
    if (xlfv1.is_open())
    {
		for(int count = 0; count < size; count ++){
            xlfv1 << xlfv[count] << " " ;
    }
		xlfv1.close();
      };
    return 0;
    }