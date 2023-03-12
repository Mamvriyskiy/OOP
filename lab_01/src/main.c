#include <stdio.h>
#include <stdlib.h>
#include "command.h"
#include "load_figure.h"

int main()
{
    struct figure_t figure;
    struct data_t data;
    data.dx = 0;
    data.dy = 0;
    data.dz = 0;
    data.kx = 0;
    data.ky = 0;
    data.kz = 0;

    figure.x_list = malloc(50 * sizeof(double));
    figure.y_list = malloc(50 * sizeof(double));
    figure.z_list = malloc(50 * sizeof(double));

    figure.len_list = 0;

    int command = 1;
    int rc = command_distribution(&figure, command, data);

    for (int i = 0; i < figure.len_list; i++)
        printf("%lf\n", figure.x_list[i]);

    free(figure.x_list);
    free(figure.y_list);
    free(figure.z_list);

    return rc;
}