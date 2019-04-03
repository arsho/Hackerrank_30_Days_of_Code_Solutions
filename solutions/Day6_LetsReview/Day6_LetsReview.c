/*
  Title     : Day 6: Let's Review
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t, cas, i, line_length;
    char line[10001]={0};
    scanf("%d",&t);
    for(cas=0;cas<t;cas++)
    {
        scanf("%s",line);
        line_length = strlen(line);
        for(i=0;i<line_length;i+=2)
            printf("%c",line[i]);
        printf(" ");
        for(i=1;i<line_length;i+=2)
            printf("%c",line[i]);
        printf("\n");
    }
    return 0;
}
