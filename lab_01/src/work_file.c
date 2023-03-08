#include <stdio.h>
#include "errors.h"

int read_len(FILE *file, int *lenl)
{
    int rc = OK;

    if (fscanf(file, "%d", lenl) != SCANF_OK)
        rc = NEGATIVE_SCANF;
    
    return rc;
}


int read_point(FILE *file, double **point, int lenl)
{
    int rc = OK;

    for (int i = 0; i < lenl && !rc; i++)
    {
        if (fscanf(file, "%lf %lf %lf", &point[0][i], &point[1][i], &point[2][i]) != SCANF_OK_THREE)
            rc = NEGATIVE_SCANF;
    }

    return rc;
}

int read_connect(FILE *file, int **connect, int lenl)
{
    int rc = OK;

    for (int i = 0; i < lenl && !rc; i++)
    {
        if (fscanf(file, "%d %d", &connect[0][i], &connect[1][i]) != SCANF_OK_TWO)
            rc = NEGATIVE_SCANF;
    }

    return rc;
}
