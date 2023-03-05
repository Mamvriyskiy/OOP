#include <stdio.h>
#include <stdlib.h>
#include "load_figure.h"
#include "work_file.h"
#include "errors.h"

int load_figure_ex(struct figure_t *figure)
{
    int rc = OK;

    char *name_file = "./data/data_1.txt";
    int len_point, len_connect;

    rc = read_len(&len_point);


    return rc;
}
