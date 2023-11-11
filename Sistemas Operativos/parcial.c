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


int main(int argc, char* args[]) {

  //MEMORIA COMPARTIDA
 
  const int SIZE = 4096;    // Tamaño en bytes que tendrá el área de memoria compartida
  const char *name = "OS";  // Nombre del área de memoria compartida
  int fd;                   // Descriptor de archivo del área de memoria compartida

 
  //Se crea el área de memoria compartida
  fd = shm_open(name, O_CREAT | O_RDWR, 0666);
  if (fd == -1) {
    perror("Error en shm_open");
    return(-1);
  }
  char *ptr;                // Puntero al área de memoria compartida

  ftruncate(fd, SIZE); //Se establece el tamaño del área de memoria compartida

  //Se mapea el área de memoria compartida
  ptr = mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  if (ptr == MAP_FAILED) {
    perror("Error MAP_FAILED");
    return (-1);
  }

  //SEMÁFOROS

  sem_t *sem;
  sem = sem_open("SEM", O_CREAT, 0666, 1); // se crea el semáforo inicializado a 1
 
  int rc = fork(); // Creación proceso hijo
 
  if (rc < 0) { // Falla creación proceso hijo
   
    printf("Falló fork()\n");
    exit(1);

  } else if (rc == 0) { // Proceso hijo: nuevo proceso
   
   

  } else { // Proceso padre sigue por aquí
      while (1){
       
      }
   
  }
 
  return 0;
}