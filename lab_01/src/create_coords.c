#include <stdio.h>
#include "command.h"
#include "load_figure.h"
#include "create_coords.h"

void create_matrix_coords(struct figure_t *figure, double **matrix, connect_array_t connect_struct)
{
    int lenl = connect_struct.lenl;

    printf("%d", lenl);
    for (int i = 0; i < lenl; i++)
    {
        int x = connect_struct.list[0][i];
        int y = connect_struct.list[1][i];

        add_coords_ex(figure, matrix, x);
        add_coords_ex(figure, matrix, y);
        add_coords_ex(figure, matrix, x);

    }
}

void add_coords_ex(struct figure_t *figure, double **matrix, int index)
{
    int k = figure->len_list;
    figure->x_list[k] = matrix[0][index];
    figure->y_list[k] = matrix[1][index];
    figure->z_list[k] = matrix[2][index];

    (figure->len_list)++;
}

// void transfer_figure(struct figure_t *figure, struct data_t data)
// {
//     int lenl = figure->len_list;
//     for (int i = 0; i < lenl; i++)
//         change_coords_plus(&(figure->list), i, data);
// }

// void change_coords_plus(struct points_t *list, int k, struct data_t data)
// {
//     list->x_list[k] += data.dx;
//     list->y_list[k] += data.dy;
//     list->z_list[k] += data.dz;
// }

// void scaling_figure(struct figure_t *figure)
// {
//     int lenl = figure->len_list;
//     for (int i = 0; i < lenl; i++)
//         change_coords_mult(figure, i);
// }

// void change_coords_mult(struct figure_t *figure, int k)
// {
//     figure->list.x_list[k] *= figure->dx;
//     figure->list.y_list[k] *= figure->dy;
//     figure->list.z_list[k] *= figure->dz;
// }
