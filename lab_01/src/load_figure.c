#include <stdio.h>
#include <stdlib.h>
#include "load_figure.h"
#include "work_file.h"
#include "allocated.h"
#include "errors.h"

int load_figure_ex(struct figure_t *figure)
{
    int rc = OK;

    points_array_t points_struct;
    connect_array_t connect_struct;

    inicialization_points_strcut(&points_struct);
    inicialization_connect_strcut(&connect_struct);
    
    rc = load_figure(&points_struct, &connect_struct);

    //преобразование матриц в массив координат фигуры

    for (int i = 0; i < points_struct.lenl; i++)
    {
        figure->list.x_list[i] = points_struct.list[0][i];
        figure->list.y_list[i] = points_struct.list[1][i];
        figure->list.z_list[i] = points_struct.list[2][i];
    }

    figure->len_list = points_struct.lenl;


    // printf("\n");

    // for (int i = 0; i < connect_struct.lenl; i++)
    //     printf("%d ", connect_struct.list[0][i]);

    if (points_struct.list)
        free_matrix_point(points_struct.list, 3);

    if (connect_struct.list)
        free_matrix_connect(connect_struct.list, 2);

    return rc;
}

int load_figure(points_array_t *points_struct, connect_array_t *connect_struct)
{
    int rc = OK;

    FILE *file = fopen("./data/data_1.txt", "r");

    if (!file)
        rc = NO_OPEN_FILE;

    if (!rc)
    {
        rc = create_point_ex(file, &(points_struct->list), &(points_struct->lenl));
        if (!rc)
            rc = create_connect_ex(file, &(connect_struct->list), &(connect_struct->lenl));

        fclose(file);
    }

    return rc;
}

int create_connect_ex(FILE *file, int ***connect_array, int *lenl)
{
    int rc = OK;

    rc = read_len(file, lenl);

    *connect_array = allocated_connect(2, *lenl);

    if (connect_array)
        rc = read_connect(file, *connect_array, *lenl);
    else
        rc = NEGATIVE_ALLOCATED;

    return rc;
}

int create_point_ex(FILE *file, double ***points_array, int *lenl)
{
    int rc = OK;

    rc = read_len(file, lenl);

    *points_array = allocated_point(3, *lenl);

    if (points_array)
        rc = read_point(file, *points_array, *lenl);
    else
        rc = NEGATIVE_ALLOCATED;

    return rc;
}
