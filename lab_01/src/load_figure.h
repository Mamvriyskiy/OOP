#ifndef _LOAD_FIGURE_H_
#define _LOAD_FIGURE_H_

#include "command.h"

typedef struct points_array 
{
    double **list;
    int lenl;
} points_array_t;

typedef struct connect_array 
{
    int **list;
    int lenl;
} connect_array_t;

int load_figure_ex(struct figure_t *figure);
int load_figure(points_array_t *points_struct, connect_array_t *connect_struct);

int create_point_ex(FILE *file, double ***points_array, int *lenl);
int create_connect_ex(FILE *file, int ***points_array, int *lenl);

#endif
