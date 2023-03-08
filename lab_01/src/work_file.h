#ifndef _WORK_FILE_H_
#define _WORK_FILE_H_

#include "command.h"

int read_len(FILE *file, int *lenl);
int read_point(FILE *file, double **array, int lenl);
int read_connect(FILE *file, int **array, int lenl);

#endif
