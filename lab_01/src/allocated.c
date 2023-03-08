#include <stdio.h>
#include <stdlib.h>
#include "allocated.h"
#include "load_figure.h"

double **allocated_point(int n, int m)
{
    double **data = malloc(m * sizeof(double*));

    if (!data)
        return NULL;
    
    for (int i = 0; i < n; i++)
    {
        data[i] = malloc(n * sizeof(double));
        if (!data[i])
        {
            free_matrix_point(data, m);
            return NULL;
        }
    }

    return data;
}

int **allocated_connect(int n, int m)
{
    int **data = malloc(m * sizeof(int*));

    if (!data)
        return NULL;
    
    for (int i = 0; i < n; i++)
    {
        data[i] = malloc(n * sizeof(int));
        if (!data[i])
        {
            free_matrix_connect(data, m);
            return NULL;
        }
    }

    return data;
}

void free_matrix_point(double **data, int n)
{
    for (int i = 0; i < n; i++)
        free(data[i]);
    
    free(data);
}

void free_matrix_connect(int **data, int n)
{
    for (int i = 0; i < n; i++)
        free(data[i]);
    
    free(data);
}

void inicialization_connect_strcut(connect_array_t *a)
{
    a->list = NULL;
    a->lenl = 0;
}

void inicialization_points_strcut(points_array_t *a)
{
    a->list = NULL;
    a->lenl = 0;
}
