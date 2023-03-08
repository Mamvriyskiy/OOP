#include <stdio.h>
#include "errors.h"
#include "command.h"

int read_len(FILE *file, int *lenl)
{
    int rc = OK;

    if (fscanf(file, "%d", lenl) != SCANF_OK)
        rc = NEGATIVE_SCANF;
    
    return rc;
}

int read_point(FILE *file, double **array, int lenl)
{
    int rc = OK;;

    for (int i = 0; i < lenl && !rc; i++)
    {
        if (fscanf(file, "%lf %lf %lf", &array[0][i], &array[1][i], &array[2][i]) != SCANF_OK_THREE)
            rc = NEGATIVE_SCANF;
    }

    return rc;
}

int read_connect(FILE *file, int **array, int lenl)
{
    int rc = OK;;

    for (int i = 0; i < lenl && !rc; i++)
    {
        if (fscanf(file, "%d %d", &array[0][i], &array[1][i]) != SCANF_OK_TWO)
            rc = NEGATIVE_SCANF;
    }

    return rc;
}
