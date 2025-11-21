#ifndef FILE_UTILS_H
#define FILE_UTILS_H

/**
 * Reads the entire content of a file into a dynamically allocated string.
 *
 * @param filename The path to the file.
 * @return A char* pointer to the string buffer, or NULL on failure.
 * The caller is responsible for freeing the returned pointer.
 */
char *read_file_to_string(const char *filename);

#endif