#include <stdio.h>
#include <stdlib.h>
#include "command.h"

int main()
{

    struct figure_t figure;
    figure.command = 1;
    figure.len_list = 0;
    figure.list.x_list = malloc(50 * sizeof(double));
    figure.list.y_list = malloc(50 * sizeof(double));
    figure.list.z_list = malloc(50 * sizeof(double));

    int rc = command_distribution(&figure);
    printf("%d", rc);

    // for (int i = 0; i < figure.len_list; i++)
    //     printf("%lf\n", figure.list.x_list[i]);

    free(figure.list.x_list);
    free(figure.list.y_list);
    free(figure.list.z_list);

    return 0;
}
