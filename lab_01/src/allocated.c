#include <stdio.h>
#include <stdlib.h>
#include "allocated.h"

double *allocated_point(int lenl)
{
    double *data = malloc(3 * lenl * sizeof(double));

    return data;
}

int *allocated_connect(int lenl)
{
    int *data = malloc(3 * lenl * sizeof(int));

    return data;
}