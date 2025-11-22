#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../common/file_utils.h"

typedef struct {
    signed short x;
    signed short y;
} Coordinate;

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

    // Warning: If input is too large this will lead to a crash
    Coordinate coordinates[2000];
    coordinates[0] = (Coordinate){0,0};
    unsigned short coordinates_length = 1;

    int found = 0;
    Coordinate solution;

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

        for(int i = 1; i < distance + 1; i++) {

            // Add distance
            x_position += x_direction;
            y_position += y_direction;

            Coordinate coordinate = {x_position, y_position};

            // Check if coordinate is visited the second time
            for(int j = 0; j < coordinates_length; j++) {
                Coordinate c_cord = coordinates[j];
                if(c_cord.x == coordinate.x && c_cord.y == coordinate.y) {
                    solution = coordinate;
                    found = 1;
                    break;
                }
            }

            // Break if solution was found
            if(found == 1) {
                break;
            }

            // Add current cords to cord array otherwise
            coordinates[coordinates_length] = coordinate;
            coordinates_length++;
        }

        printf("New x:%d y:%d direction\n", x_direction, y_direction);
        printf("New x:%d y:%d position\n", x_position, y_position);

        if(found == 1) {
            break;
        }

        token = strtok(NULL, delimiter);
    }

    unsigned short total_distance = abs(x_position) + abs(y_position);
    printf("(%d, %d)\n", solution.x, solution.y);
    printf("Distance: %d", total_distance);

    // Free the allocated memory
    free(file_content);

    return 1;
}