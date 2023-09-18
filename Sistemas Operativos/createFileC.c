#include <stdio.h>

int main()
{

    FILE *hFile = NULL;
    const char filename[] = "archivo.txt";

    hFile = fopen(filename, "a");
    if (hFile == NULL)
    {

        return 2;
    }

    fclose(hFile);
}