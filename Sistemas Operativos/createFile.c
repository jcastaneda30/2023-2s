#include <windows.h>
#include <stdio.h>

int main() {
    // Definimos el nombre del archivo como una cadena de caracteres amplios (LPCWSTR)
    LPCSTR  filename = "archivo.txt";
    
    // Declaramos una variable para el manejador del archivo
    HANDLE hFile;
    
    // Creamos el archivo "archivo.txt" con permisos de escritura
    hFile = CreateFile(
        filename,                   // Nombre del archivo
        GENERIC_WRITE,              // Permiso de escritura
        0,                          // No se comparte con otros procesos
        NULL,                       // Atributos de seguridad (nulos en este caso)
        CREATE_ALWAYS,              // Si el archivo existe, lo sobrescribe; si no, lo crea
        FILE_ATTRIBUTE_NORMAL,      // Atributos del archivo (normal en este caso)
        NULL                        // Manija de plantilla (nulo en este caso)
    );

    // Verificamos si la creación del archivo fue exitosa
    if (hFile == INVALID_HANDLE_VALUE) {
        // En caso de error, retornamos un código de error (en este caso, 2)
        return 2;
    }

    // Cerramos el manejador del archivo
    CloseHandle(hFile);

    // Indicamos que la operación se completó exitosamente
    return 0;
}
