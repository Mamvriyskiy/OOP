#ifndef _ALLOCATED_H_
#define _ALLOCATED_H_

double **allocated_point(int n, int m);
int **allocated_connect(int n, int m);

void free_matrix_connect(int **data, int n);
void free_matrix_point(double **data, int n);

#endif
