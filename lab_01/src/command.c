#include <stdio.h>
#include <stdlib.h>
#include "command.h"
#include "load_figure.h"
#include "errors.h"

int command_distribution(struct figure_t *figure)
{
    int error = OK;
    int command = figure->command;

    if (command == LOAD_FIGURE)
        error = load_figure_ex(figure);
    else 
        error = convert_figure(figure);

    return error;
}


int convert_figure(struct figure_t *figure)
{
    int convert = figure->command;

    if (convert == TRANSFER_FIGURE)
        return 0;
    else if (convert == TURN_FIGURE)
        return 0;
    else if (convert == SCALE_FIGURE)
        return 0;

    return 0;
}


