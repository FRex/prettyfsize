#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "../c/prettyfsize.h"

#include <fcntl.h>
#include <io.h>

static int samestring(const char * a, const char * b) {return 0 == strcmp(a, b);}

int main(int argc, char ** argv)
{
    /* force windows stdout to not use \r\n but \n only */
    setmode(fileno(stdout), O_BINARY);

    if(argc == 4 && samestring(argv[2], "to"))
    {
        long long a = strtoll(argv[1], NULL, 10);
        long long b = strtoll(argv[3], NULL, 10);

        while(a <= b)
        {
            char buff[100];
            prettyfsize(buff, (double)a);
            printf("%s\n", buff);
            ++a;
        }
    }

    return 0;
}
