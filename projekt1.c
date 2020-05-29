#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
#include <math.h>
#include <windows.h>
#define pi 3.141592
void menu();
void tablicowanie1(char px[][15], char funkcja[][15], int *pN);
void tablicowanie2(char px[][15], char funkcja[][15], int *pN);
void wczytywanieDanychWariant1(double *pA,double *pB,int *ppN,int *pK);
void wczytywanieDanychWariant2(double *pA,double *pdelta,int *ppN,int *pK);
void przegladanieTabFun();
double wczytajLiczbeDouble();
int wczytajLiczbeInt();
int nalezyDoDziedziny(double z);
double obliczFun(double x,int k);
char x[100][15],funkcja[100][15];
int main()
{
	while(1) menu();
	return 0;
}
void menu()
{
	char ch;
	int N,i;
	system("cls");
	printf("====================================\n");
	printf("1.Tablicowanie w zadanym przedziale [a,b] w N punktach\n");
	printf("2.Tablicowanie od zadanego punktu a w N punktach co krok delta\n");
	printf("3.Wyjscie lub ESC\n");
	printf("====================================\n");
	fflush(stdin);
	do 
	{
		ch=getch();
		fflush(stdin);
	}while ( ch!='1' && ch!= '2'&& ch!='3'&& ch!=27);
	if (ch=='1')
	{
		printf("1");
		getchar();
		system("cls");
		tablicowanie1(x,funkcja, &N);
		for(i=0;i<N;i++)
		{
			printf("\n%s",funkcja[i]);
			printf("\n%i",i);
		}
		getch();
		//przegladanieTabFun(x,funkcja,N);
	}
	if (ch=='2')
	{
		printf("2");
		getchar();
		system("cls");
		tablicowanie2(x,funkcja, &N);
		for(i=0;i<N;i++)
		{
			printf("\n%s",funkcja[i]);
			printf("\n%i",i);
		}
		getch();
		//przegladanieTabFun(x,funkcja, N);
	}
	if (ch==27 || ch=='3')
	{
		printf("3");
		getchar();
		exit(0);
	}
}
void tablicowanie1(char px[][15], char funkcja[][15], int *pN)
{
	system("cls");
	double a,b,x;
	int i,k;
	printf("Tablicowanie wariant 1\n");
	printf("w przedzale <a,b> w N punktach\n");
	wczytywanieDanychWariant1(&a,&b,pN,&k);
	double delta=(b-a)/(*pN-1);
	for (i=0;i<*pN;i++)
	{
		x=a+i*delta;
		sprintf(px[i], "%8.2f", x);
		if (nalezyDoDziedziny(x))
		{
			double fx=obliczFun(x,k);
			sprintf(funkcja[i], "%8.2f",fx);
		}
		else strcpy(funkcja[i], "Poza dziedzina");
	}
}
void tablicowanie2(char px[][15], char funkcja[][15], int *pN)
{
	system("cls");
	double a,delta,x;
	int i,k;
	printf("Tablicowanie wariant 2\n");
	printf("od a w N punktach co krok delta\n");
	wczytywanieDanychWariant2(&a,&delta,pN,&k);
	for (i=0;i<*pN;i++)
	{
		x=a+i*delta;
		sprintf(px[i], "%8.2f", x);
		if (nalezyDoDziedziny(x))
		{
			double fx=obliczFun(x,k);
			sprintf(funkcja[i], "%8.2f",fx);
		}
		else strcpy(funkcja[i], "Poza dziedzina");
	}
}
int nalezyDoDziedziny(double z)
{
	if(z<0 || z==5 || fmod(z,pi)==0 || fmod(z,pi/2)==0) return 0;
	else return 1;
}
double obliczFun(double x,int k)
{
	double sum=0;
	int i;
	for(i=1;i<=k;i++)
	{
		sum+=exp(log10(silnia(i)));
	}
	return (sum+silnia(i)/tan(x*i))/((x-5)*(x+3));
}
int silnia(int s)
{
	if(s==0 || s==1) return 1;
	else return s*silnia(s-1);
}
void wczytywanieDanychWariant1(double *pA,double *pB,int *ppN,int *pK)
{
	printf("Podaj a: ");
	*pA=wczytajLiczbeDouble();
	printf("%lf",*pA);
	printf("\nPodaj b: ");
	*pB=wczytajLiczbeDouble();
	printf("%lf",*pB);
	do
	{
		printf("\nPodaj N: ");
		*ppN=wczytajLiczbeInt();
		printf("%i",*ppN);
		if(*ppN<=1 || *ppN>99) printf("\nLiczba musi byc wieksza od 1 i nie wieksza od 99");
	}while(*ppN<=1 || *ppN>99);
	printf("\nPodaj k: ");
	*pK=wczytajLiczbeInt();
	printf("%i",*pK);
}
void wczytywanieDanychWariant2(double *pA,double *pdelta,int *ppN,int *pK)
{
	printf("Podaj a: ");
	*pA=wczytajLiczbeDouble();
	printf("%lf",*pA);
	printf("\nPodaj delte: ");
	*pdelta=wczytajLiczbeDouble();
	printf("%lf",*pdelta);
	do
	{
		printf("\nPodaj N: ");
		*ppN=wczytajLiczbeInt();
		printf("%i",*ppN);
		if(*ppN<=1 || *ppN>99) printf("\nLiczba musi byc wieksza od 1 i nie wieksza od 99");
	}while(*ppN<=1 || *ppN>99);
	printf("\nPodaj k: ");
	*pK=wczytajLiczbeInt();
	printf("%i",*pK);
}
double wczytajLiczbeDouble()
{
	char wczytlicz[8],licz[8];
	int i,j=0;
	int kropka=0;
	for(i=0;i<8;i++)
	{
		fflush(stdin);
		wczytlicz[i]=getch();
		fflush(stdin);
		if(wczytlicz[i]==13) 
		{
			wczytlicz[i]='\0';
			break;
		}
	}
	for(i=0;i<8;i++) 
	{
		if(wczytlicz[i]=='\0') break;
		if(isdigit(wczytlicz[i]))
		{
			licz[j]=wczytlicz[i];
			j++;
		}
		else if (wczytlicz[i]=='.' && kropka==0 && i>0)
		{
			licz[j]=wczytlicz[i];
			kropka=1;
			j++;
		}
		else if ((wczytlicz[i]=='-' || wczytlicz[i]=='+') && i==0)
		{
			licz[j]=wczytlicz[i];
			j++;
		}
	}
	return atof(licz);
}
int wczytajLiczbeInt()
{
	char wczytlicz[8],licz[8];
	int i,j=0;
	int zmienna=0;
	for(i=0;i<8;i++)
	{
		fflush(stdin);
		wczytlicz[i]=getch();
		fflush(stdin);
		if(wczytlicz[i]==13) 
		{
			wczytlicz[i]='\0';
			break;
		}
	}
	for(i=0;i<8;i++) 
	{
		if(wczytlicz[i]=='\0') break;
		if(isdigit(wczytlicz[i]))
		{
			licz[j]=wczytlicz[i];
			j++;
		}
		else if ((wczytlicz[i]=='-' || wczytlicz[i]=='+') && i==0)
		{
			licz[j]=wczytlicz[i];
			j++;
		}
	}
	return atoi(licz);
}
