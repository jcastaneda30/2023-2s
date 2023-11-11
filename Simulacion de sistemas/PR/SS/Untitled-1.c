#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
int main()
{
    /* Tamaño en bytes que tendrá el área de memoria compartida */
    const int SIZE = 40096;
    /* nombre del área de memoria compartida */
    const char *name = "SUMAS";
    /* cadenas que se escribirán al área de memoria compartida */
    int *suma = 0;
    /* descriptor de archivo del área de memoria compartida */
    int fd;
    /* puntero al área de memoria compartida */
    char *ptr;
    /* se crea el área de memoria compartida */
    fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    if (fd == -1)
    {
        perror("Error en shm_open");
        return (-1);
    }
    /* se establece el tamaño del área de memoria compartida */
    ftruncate(fd, SIZE);
    /* se mapea el área de memoria compartida */
    ptr = mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (ptr == MAP_FAILED)
    {
        perror("Error MAP_FAILED");
        return (-1);
    }
    int i=0;
    for(i=1;i<51;i++){
        suma+=i;
    }
    /* Se escriben los 5 bytes de m_0 al área de memoria */
    /* compartida */
    sprintf(ptr, "%d", suma);
    /* se actualiza apuntador */
    ptr += strlen(suma);
    return 0;
}