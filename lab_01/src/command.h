#ifndef _COMMAND_H_
#define _COMMAND_H_

#define LOAD_FIGURE 1
#define TRANSFER_FIGURE 2
#define TURN_FIGURE 3
#define SCALE_FIGURE 4

struct points_t
{
    double *x_list;
    double *y_list;
    double *z_list;
};

struct figure_t {
    int command;
    struct points_t list;
    int len_list;
};

int command_distribution(struct figure_t *test);
int convert_figure(struct figure_t *figure);

#endif
