#include <stdio.h>
#include <stdlib.h>
#include "command.h"
#include "load_figure.h"
#include "errors.h"
#include "create_coords.h"

int command_distribution(struct figure_t *figure, int command, struct data_t data)
{
    int error = OK;

    if (command == LOAD_FIGURE)
        error = load_figure_ex(figure);
    // else 
    //     error = convert_figure(figure, command, data);

    // for (int i = 0; i < 1; i++)
    //     printf("%lf\n", figure->x_list[i]);

    printf("%lf", data.dx);

    return error;
}

int convert_figure(struct figure_t *figure, int command, struct data_t data)
{
    int rc = OK;

    figure->len_list = 0;
    printf("%lf %d", data.dx, command);
    // if (command == TRANSFER_FIGURE)
    //     transfer_figure(figure, data);
    // else if (command == TURN_FIGURE)
    //     return 0;
    // else if (command == SCALE_FIGURE)
    //     scaling_figure(figure);

    return rc;
}


