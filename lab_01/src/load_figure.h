#ifndef _LOAD_FIGURE_H_
#define _LOAD_FIGURE_H_

#include "command.h"

int load_figure_ex(struct figure_t *figure);
int load_figure(FILE *file, struct figure_t *figure);
int create_point_ex(FILE *file, double **point, int *lenl);
int create_connect_ex(FILE *file, int **connect, int *lenl);

#endif
