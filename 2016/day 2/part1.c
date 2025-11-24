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
    
    char *delimiter = "\n";
    char *line = strtok(file_content, delimiter);

    const char keypad[3][3] = {{'1', '2', '3'},{'4', '5', '6'},{'7', '8', '9'}};

    char x = 1;
    char y = 1;

    printf("The code is: ");

    // Iterate through the instructions
    while (line != NULL) {

        // Iterate througgh each char
        for(int i = 0; line[i] != '\0'; i++) {
            switch(line[i]) {
                case 'U':
                    if(y != 0) y--;
                    break;
                case 'R':
                    if(x != 2) x++;
                    break;
                case 'D':
                    if(y != 2) y++;
                    break;
                case 'L':
                    if(x != 0) x--;
                    break;
            }
        }

        printf("%c", keypad[y][x]);
    
        line = strtok(NULL, delimiter);
    }

    // Free the allocated memory
    free(file_content);

    return 1;
}