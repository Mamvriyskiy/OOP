#ifndef _CREATE_COORDS_H_
#define _CREATE_COORDS_H_

#include "command.h"
#include "load_figure.h"

#define THREE_LEN 3

void create_matrix_coords(struct figure_t *figure, double **matrix, connect_array_t connect_struct);

int add_coords_ex(struct figure_t *figure, double **matrix, int index);

void transfer_figure(struct figure_t *figure, struct data_t data);
// void change_coords_plus(struct points_t *list, int k, struct data_t data);

void scaling_figure(struct figure_t *figure);
void change_coords_mult(struct figure_t *figure, int k);

#endif
