#include <stdio.h>
#include <stdlib.h>
#include "load_figure.h"
#include "work_file.h"
#include "allocated.h"
#include "errors.h"

int load_figure_ex(struct figure_t *figure)
{
    int rc = OK;

    FILE *file = fopen("./data/data_1.txt", "r");

    if (!file)
        rc = NO_OPEN_FILE;
    else
    {
        rc = load_figure(file, figure);
        fclose(file);
    }

    return rc;
}

int load_figure(FILE *file, struct figure_t *figure)
{
    int rc = OK;

    if (figure->len_connect != 0)
    {
        free_matrix_connect(figure->connect, 2);
        figure->connect = NULL;
        figure->len_connect = 0;
    }

    if (figure->len_point != 0)
    {
        free_matrix_point(figure->point, 3);
        figure->point = NULL;
        figure->len_point = 0;
    }

    rc = create_point_ex(file, &(figure->point), &(figure->len_point));

    if (!rc)
        rc = create_connect_ex(file, &(figure->connect), &(figure->len_connect)); 

    return rc;
}

int create_point_ex(FILE *file, double ***point, int *lenl)
{
    int rc = OK;

    rc = read_len(file, lenl);

    if (!rc && !*point)
        *point = allocated_point(*lenl, 3);

    if (*point)
        rc = read_point(file, *point, *lenl);
    else
        rc = NEGATIVE_ALLOCATED;

    return rc;
}

int create_connect_ex(FILE *file, int ***connect, int *lenl)
{
    int rc = OK;

    rc = read_len(file, lenl);

    if (!rc)
        *connect = allocated_connect(*lenl, 2);

    if (*connect)
        rc = read_connect(file, *connect, *lenl);
    else
        rc = NEGATIVE_ALLOCATED;

    return rc;
}
