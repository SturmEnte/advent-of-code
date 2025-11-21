#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../common/file_utils.h"

int main(int argc, char *argv[]) {

    // The first argument (excluding the execution) is the input file name
    char *my_file = argv[1];
    char *file_content = NULL;

    file_content = read_file_to_string(my_file);

    if (file_content == NULL) {
        return 0;
    }

    printf("--- File Content ---\n%s\n--- End of File ---\n", file_content);
    
    // Seperate the input on ", "
    char *delimiter = ", ";
    char *token = strtok(file_content, delimiter);

    // y 1 norht -1 south
    // x 1 east -1 west
    signed char x_direction = 0;
    signed char y_direction = 1;

    signed short x_position = 0;
    signed short y_position = 0;

    signed char x_cache;

    // Iterate through the instructions
    while (token != NULL) {
        char direction = token[0];
        // Token is a pointer to a address in the original char array
        // By adding 1 it just moves one adress to the right from the first one
        // This way it ignores the letter
        // The function know when the string/char array has ended because the end is marked by a \0
        unsigned short distance = atoi(token + 1);

        printf("Direction: %c, Distance: %d\n", direction, distance);
        
        switch(direction) {
            case 'R':
                x_cache = x_direction;
                x_direction = y_direction;
                y_direction = -x_cache;
                break;
            case 'L':
                x_cache = x_direction;
                x_direction = -y_direction;
                y_direction = x_cache;
                break;
            default:
                break;
        }

        x_position += distance * x_direction;
        y_position += distance * y_direction;

        printf("New x:%d y:%d direction\n", x_direction, y_direction);
        printf("New x:%d y:%d position\n", x_position, y_position);

        token = strtok(NULL, delimiter);
    }

    unsigned short total_distance = abs(x_position) + abs(y_position);
    printf("Distance: %d", total_distance);

    // Free the allocated memory
    free(file_content);

    return 1;
}