/*
  Title     : Day 1: Data Types
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";

    int a;
    float b;
    char c[500]={0};
    scanf("%d",&a);
    scanf("%f",&b);
    gets(c);
    gets(c);
    printf("%d\n",a+i);
    printf("%.1f\n",d+b);
    printf("%s%s\n",s,c);
    return 0;
}
