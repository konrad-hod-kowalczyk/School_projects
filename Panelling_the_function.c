
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
#include <math.h>
//this two libraries are for possibility to use unicode in console to print out arrows
#include <fcntl.h>
#include <io.h>
#define pi 3.141592
void menu();
void tablicowanie1(char px[][15], char funkcja[][15], int *pN);
void tablicowanie2(char px[][15], char funkcja[][15], int *pN);
void wczytywanieDanychWariant1(double *pA,double *pB,int *ppN,int *pK);
void wczytywanieDanychWariant2(double *pA,double *pdelta,int *ppN,int *pK);
void przegladanieTabFun(char px[][15], char funkcja[][15],int n);
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
	printf("1.Panelling in given interval <a;b> in N points\n");
	printf("2.Panneling from given point a in N points with delta step\n");
	printf("3.Exit or ESC\n");
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
		przegladanieTabFun(x,funkcja,N);
	}
	if (ch=='2')
	{
		printf("2");
		getchar();
		system("cls");
		tablicowanie2(x,funkcja, &N);
		przegladanieTabFun(x,funkcja, N);
	}
	if (ch==27 || ch=='3')
	{
		printf("3");
		getchar();
		exit(0);
	}
}
void przegladanieTabFun(char px[][15], char funkcja[][15],int n)
{
	char wyn[n+1][3][15];
	char ch1,ch2;
	int start=1,koniec;
	if (n>10) koniec=10;
	else koniec=n;
	strcpy(wyn[0][0],"Punkt");
	strcpy(wyn[0][1],"Liczba x");
	strcpy(wyn[0][2],"f(x)");
	int i;
	for(i=1;i<n+1;i++)
	{
		itoa(i,wyn[i][0],10);
		strcpy(wyn[i][1],px[i-1]);
		strcpy(wyn[i][2],funkcja[i-1]);
	}
	do
	{
		system("cls");
		printf("\n%s	%s	  %s",wyn[0][0],wyn[0][1],wyn[0][2]);
		for(i=start;i<koniec+1;i++)
		{
			printf("\n%s	",wyn[i][0]);
			printf("%s	",wyn[i][1]);
			printf("%s",wyn[i][2]);
		}
		do
		{
			printf("\n Podaj klawisz funkcyjny:");
			_setmode(_fileno(stdout),_O_U16TEXT);
			wprintf(L"\nArrowDn \xa71c ArrowUp \xa71b PgDn PgUp Home End Esc-exit");
			_setmode(_fileno(stdout),_O_TEXT);
			fflush(stdin);
			ch1=getch();
			if(ch1==27) break;
			ch2=getch();
		}while (ch1!=-32);
		if (ch2==73 || ch2==72) 
		{
			//PgUp or arrow up
			if(koniec==n && n>10 && n%10!=0)
			{
				start-=10;
				koniec-=koniec%10;
			}
			else if(koniec==n && n>10 && n%10==0)
			{
				start-=10;
				koniec-=10;
			}
			else if(start>10)
			{
				start-=10;
				koniec-=10;
			}
			else
			{
				start=1;
				if (n>10) koniec=10;
				else koniec=n;
			}
		}
		if (ch2==81 || ch2==80)
		{
			//PgDown or arrow down
			if(koniec<n-10)
			{
				start+=10;
				koniec+=10;
			}
			else if(n%10==0)
			{
				koniec=n;
				start=koniec-9;
			}
			else
			{
				koniec=n;
				start=koniec-(koniec%10)+1;
			}
		}
		if (ch2==71) 
		{
			//Home
			start=1;
			if (n>10) koniec=10;
			else koniec=n;
		}
		if (ch2==79) 
		{
			//End
			if(n%10==0)
			{
				koniec=n;
				start=koniec-9;
			}
			else
			{
				koniec=n;
				start=koniec-(koniec%10)+1;
			}
		}
	}while(ch1!=27);
}
void tablicowanie1(char px[][15], char funkcja[][15], int *pN)
{
	system("cls");
	double a,b,x;
	int i,k;
	printf("Panelling variant 1\n");
	printf("in interval <a,b> in N points\n");
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
		else strcpy(funkcja[i], "not in domain");
	}
}
void tablicowanie2(char px[][15], char funkcja[][15], int *pN)
{
	system("cls");
	double a,delta,x;
	int i,k;
	printf("Panelling variant 2\n");
	printf("from a in N points with delta step\n");
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
		else strcpy(funkcja[i], "not in domain");
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
		sum+=exp(log10(silnia(i)))+silnia(i)/tan(x*i);
	}
	return sum/((x-5)*(x+3));
}
int silnia(int s)
{
	if(s==0 || s==1) return 1;
	else return s*silnia(s-1);
}
void wczytywanieDanychWariant1(double *pA,double *pB,int *ppN,int *pK)
{
	printf("Insert a: ");
	*pA=wczytajLiczbeDouble();
	printf("%lf",*pA);
	printf("\nInsert b: ");
	*pB=wczytajLiczbeDouble();
	printf("%lf",*pB);
	do
	{
		printf("\nInsert N: ");
		*ppN=wczytajLiczbeInt();
		printf("%i",*ppN);
		if(*ppN<=1 || *ppN>99) printf("\nIntegral must be greater than 1 and lower than 99");
	}while(*ppN<=1 || *ppN>99);
	printf("\nInsert k: ");
	*pK=wczytajLiczbeInt();
	printf("%i",*pK);
}
void wczytywanieDanychWariant2(double *pA,double *pdelta,int *ppN,int *pK)
{
	printf("Insert a: ");
	*pA=wczytajLiczbeDouble();
	printf("%lf",*pA);
	printf("\nInsert delta: ");
	*pdelta=wczytajLiczbeDouble();
	printf("%lf",*pdelta);
	do
	{
		printf("\nPodaj N: ");
		*ppN=wczytajLiczbeInt();
		printf("%i",*ppN);
		if(*ppN<=1 || *ppN>99) printf("\nIntegral must be greater than 1 and lower than 99");
	}while(*ppN<=1 || *ppN>99);
	printf("\nInsert k: ");
	*pK=wczytajLiczbeInt();
	printf("%i",*pK);
}
double wczytajLiczbeDouble()
{
	char wczytlicz[9],licz[9];
	int i,j=0;
	int kropka=0;
	for(i=0;i<9;i++)
	{
		fflush(stdin);
		wczytlicz[i]=getch();
		fflush(stdin);
		if(wczytlicz[i]==13 || i==8) 
		{
			wczytlicz[i]='\0';
			break;
		}
	}
	for(i=0;i<9;i++) 
	{
		if(wczytlicz[i]=='\0') break;
		if(isdigit(wczytlicz[i]))
		{
			licz[j]=wczytlicz[i];
			j++;
		}
		else if (wczytlicz[i]=='.' && kropka==0 && j>0)
		{
			licz[j]=wczytlicz[i];
			kropka=1;
			j++;
		}
		else if ((wczytlicz[i]=='-' || wczytlicz[i]=='+') && j==0)
		{
			licz[j]=wczytlicz[i];
			j++;
		}
	}
	return atof(licz);
}
int wczytajLiczbeInt()
{
	char wczytlicz[9],licz[9];
	int i,j=0;
	int zmienna=0;
	for(i=0;i<9;i++)
	{
		fflush(stdin);
		wczytlicz[i]=getch();
		fflush(stdin);
		if(wczytlicz[i]==13 || i==8) 
		{
			wczytlicz[i]='\0';
			break;
		}
	}
	for(i=0;i<9;i++) 
	{
		if(wczytlicz[i]=='\0') break;
		if(isdigit(wczytlicz[i]))
		{
			licz[j]=wczytlicz[i];
			j++;
		}
		else if ((wczytlicz[i]=='-' || wczytlicz[i]=='+') && j==0)
		{
			licz[j]=wczytlicz[i];
			j++;
		}
	}
	return atoi(licz);
}
