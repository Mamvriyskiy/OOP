#include <stdio.h>
#include "errors.h"

int read_len(FILE *file, int *lenl)
{
    int rc = OK;

    if (fscanf(file, "%d", lenl) != SCANF_OK)
        rc = NEGATIVE_SCANF;
    
    return rc;
}
