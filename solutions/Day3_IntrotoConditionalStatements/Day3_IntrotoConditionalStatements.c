/*
  Title     : Day 3: Intro to Conditional Statements
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
*/
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();



int main()
{
    char* N_endptr;
    char* N_str = readline();
    int N = strtol(N_str, &N_endptr, 10);
    char* w = "Weird";
    char* nw = "Not Weird";
    if(N%2==1)
        printf("%s\n",w);
    else
    {
        if((2<=N)&&(N<=5))
            printf("%s\n",nw);
        else if((6<=N)&&(N<=20))
            printf("%s\n",w);
        else
            printf("%s\n",nw);
    }
    if (N_endptr == N_str || *N_endptr != '\0') { exit(EXIT_FAILURE); }

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}
