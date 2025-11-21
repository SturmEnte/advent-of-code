#include <stdio.h>
#include <stdlib.h>
#include "file_utils.h"

/**
 * Reads the entire content of a file into a dynamically allocated string.
 *
 * @param filename The path to the file.
 * @return A char* pointer to the string buffer, or NULL on failure.
 * The caller is responsible for freeing the returned pointer.
 */
char *read_file_to_string(const char *filename) {
    FILE *file = NULL;
    long file_size = 0;
    char *buffer = NULL;
    size_t result = 0;

    file = fopen(filename, "rb"); 
    if (file == NULL) {
        perror("Error opening file");
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    buffer = (char *)malloc((file_size + 1) * sizeof(char));
    if (buffer == NULL) {
        perror("Memory allocation failed");
        fclose(file);
        return NULL;
    }

    result = fread(buffer, file_size, 1, file);
    if (result != 1) {
        perror("Error reading file content");
        free(buffer);
        fclose(file);
        return NULL;
    }

    buffer[file_size] = '\0'; 
    fclose(file);

    return buffer;
}