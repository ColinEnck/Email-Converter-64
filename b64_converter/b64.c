/*
    BASE64 TEXT ENCODER
    **INCOMPLETE**
    Author --  Colin Enck
    Date -- 3/24/2024
    _____________________
    1st arg is encode/decode (-e/-d)
    2nd is input file
    3rd is output file
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void usage();

int main(int argc, char const *argv[])
{
    if (argc != 4)
    {
        usage();
        return 0;
    }

    FILE *in, *out;
    char *code = NULL;
    size_t n = 0;
    char table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

    in = fopen(argv[2], "r");
    if (in == NULL)
    {
        printf("Error opening input file\n");
        return 1;
    }
    if (getline(&code, &n, in) == -1)
    {
        printf("Error reading input file\n");
        return 1;
    }

    out = fopen(argv[3], "w");
    if (out == NULL)
    {
        printf("Error opening output file\n");
        return 1;
    }

    if (strcmp(argv[1], "-e") == 0)
    {
        
    }
    else if (strcmp(argv[1], "-d") == 0)
    {

    }
    else usage();

    fclose(in);
    fclose(out);
    
    return 0;
}

void usage()
{
    printf("USAGE:\n");
    printf("1st arg is encode/decode (-e/-d)\n2nd is input file\n3rd is output file\n");
}
