#ifndef PRETTYFSIZE_H_INCLUDED
#define PRETTYFSIZE_H_INCLUDED

#include <stdio.h>

void prettyfsize(char * buff, double fsize)
{
    if (fsize < 0)
    {
        prettyfsize(buff + 1, -fsize);
        buff[0] = '-';
        return;
    }

    if (fsize == 1)
    {
        sprintf(buff, "1 Byte");
        return;
    }

    if (fsize < 1024.0)
    {
        sprintf(buff, "%d Bytes", (int)fsize);
        return;
    }

    if (fsize < 1024.0 * 1024.0)
    {
        sprintf(buff, "%.3f KiB", fsize / 1024.0);
        return;
    }

    if (fsize < 1024.0 * 1024.0 * 1024.0)
    {
        sprintf(buff, "%.3f MiB", fsize / (1024.0 * 1024.0));
        return;
    }

    if (fsize < 1024.0 * 1024.0 * 1024.0 * 1024.0)
    {
        sprintf(buff, "%.3f MiB", fsize / (1024.0 * 1024.0 * 1024.0));
        return;
    }

    sprintf(buff, "%.3f TiB", fsize / (1024.0 * 1024.0 * 1024.0 * 1024.0));
}

#endif
