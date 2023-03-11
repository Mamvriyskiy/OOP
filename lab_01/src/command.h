#ifndef _COMMAND_H_
#define _COMMAND_H_

#define LOAD_FIGURE 1
#define TRANSFER_FIGURE 2
#define TURN_FIGURE 3
#define SCALE_FIGURE 4

struct data_t {
    double kx;
    double ky;
    double kz;
    double dx;
    double dy;
    double dz;
};

struct figure_t {
    double *x_list;
    double *y_list;
    double *z_list;
    int len_list;
};

int command_distribution(struct figure_t *figure, int command, struct data_t data);
int convert_figure(struct figure_t *figure, int command, struct data_t data);

#endif
