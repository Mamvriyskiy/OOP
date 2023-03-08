#ifndef _ALLOCATED_H_
#define _ALLOCATED_H_

#include "load_figure.h"

double **allocated_point(int n, int m);
int **allocated_connect(int n, int m);

void free_matrix_connect(int **data, int n);
void free_matrix_point(double **data, int n);

void inicialization_points_strcut(points_array_t *a);
void inicialization_connect_strcut(connect_array_t *a);

#endif
