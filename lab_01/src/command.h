#ifndef _COMMAND_H_
#define _COMMAND_H_

#define LOAD_FIGURE 1
#define TRANSFER_FIGURE 2
#define TURN_FIGURE 3
#define SCALE_FIGURE 4

struct figure_t {
    int command;
    double a;
    double b;
    double c;
    double *point;
    int *connect;
    int len_point;
    int len_connect;
};

int command_distribution(struct figure_t *test);
int convert_figure(struct figure_t *figure);

#endif
