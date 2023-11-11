/*Maria Fernanda Calle Agudelo
  Jaider Castañeda Villa*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <semaphore.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <ctype.h>

int main(int argc, char *args[])
{

    const int SIZE = 4096;   // Tamaño en bytes que tendrá el área de memoria compartida
    const char *name = "OS"; // Nombre del área de memoria compartida
    int fd;

    fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    if (fd == -1)
    {
        perror("Error en shm_open");
        return (-1);
    }

    ftruncate(fd, SIZE); // Se establece el tamaño del área de memoria compartida
    char *ptr;           // Puntero al área de memoria compartida

    // Se mapea el área de memoria compartida
    ptr = mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (ptr == MAP_FAILED)
    {
        perror("Error MAP_FAILED");
        return (-1);
    }

    sem_t *sem;
    sem = sem_open("SEM", O_CREAT, 0666, 1); // se crea el semáforo inicializado a 1
    sem_t *sem1;
    sem1 = sem_open("SEM1", O_CREAT, 0666, 1); // se crea el semáforo inicializado a 1

    int rc = fork();
    // Creación proceso hijo
    if (rc < 0)
    { // Falla creación proceso hijo
        printf("Falló fork()\n");
        exit(1);
    }
    if (rc == 0)
    {

        sem = sem_open("SEM", O_CREAT, 0666, 1);
        sem1 = sem_open("SEM1", O_CREAT, 0666, 1);

        fd = shm_open(name, O_RDWR, 0666);
        if (fd == -1)
        {
            perror("Error en shm_open");
            return -1;
        }
        ptr = mmap(0, SIZE, PROT_READ, MAP_SHARED, fd, 0);
        if (ptr == MAP_FAILED)
        {
            perror("Error MAP_FAILED");
            return -1;
        }

        while (1)
        {

            if (rc > 0)
            {
                char *linea = NULL;
                size_t capacidad = 0;
                printf("Ingrese cadena de texto: ");
                getline(&linea, &capacidad, stdin);
                sprintf((char *)ptr, "%s", linea);
                sem_post(sem);
                sem_wait(sem1);
                char cadena[SIZE];
                strcpy(cadena, ptr);
                printf("Proceso padre recibe de regreso: %s\n", cadena);
            }
            if (rc == 0)
            {
                sem_wait(sem);
                char cadena[SIZE];
                strcpy(cadena, ptr);
                // Lo pasa a mayusculas

                printf("Proceso hijo recibe: %s\n", cadena);
                for (int i = 0; i < SIZE; i++)
                {
                    cadena[i] = toupper(cadena[i]);
                }
                printf("Arreglo en mayúsculas: %s\n", cadena);
                sprintf((char *)ptr, "%s", cadena);
                sem_post(sem1);
            }
        }
    }
}