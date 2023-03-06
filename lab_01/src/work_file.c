#include <stdio.h>
#include "errors.h"

int read_len(FILE *file, int *lenl)
{
    int rc = OK;

    if (fscanf(file, "%d", lenl) != SCANF_OK)
        rc = NEGATIVE_SCANF;
    
    (*lenl) *= 3;
    
    return rc;
}


int read_point(FILE *file, double *point, int lenl)
{
    int rc = OK;

    for (int i = 0; i < lenl && !rc; i++)
    {
        if (fscanf(file, "%lf %lf %lf", &point[i], &point[i + 1], &point[i + 2]) != SCANF_OK_THREE)
            rc = NEGATIVE_SCANF;
    }

    return rc;
}

int read_connect(FILE *file, int *connect, int lenl)
{
    int rc = OK;

    for (int i = 0; i < lenl && !rc; i++)
    {
        if (fscanf(file, "%d %d %d", &connect[i], &connect[i + 1], &connect[i + 2]) != SCANF_OK_THREE)
            rc = NEGATIVE_SCANF;
    }

    return rc;
}
