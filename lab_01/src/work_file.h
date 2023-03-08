#ifndef _WORK_FILE_H_
#define _WORK_FILE_H_

int read_len(FILE *file, int *lenl);
int read_connect(FILE *file, int **connect, int lenl);
int read_point(FILE *file, double **point, int lenl);

#endif
