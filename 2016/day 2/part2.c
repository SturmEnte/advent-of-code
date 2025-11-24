#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../common/file_utils.h"

int is_button(int x, int y) {
    if(abs(x) + abs(y) <= 2) return 1;
    return 0;
}

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

    const char keypad[5][5] = {
        {'\0', '\0', '1', '\0', '\0'},
        {'\0',  '2', '3',  '4', '\0'},
        { '5',  '6', '7',  '8',  '9'},
        {'\0',  'A', 'B',  'C', '\0'},
        {'\0', '\0', 'D', '\0', '\0'} 
    };

    // 0 0 is the middle
    signed char x = -2;
    signed char y = 0;

    const char offset = 2;

    printf("The code is: ");

    // Iterate through the instructions
    while (line != NULL) {

        // Iterate througgh each char
        for(int i = 0; line[i] != '\0'; i++) {
            switch(line[i]) {
                case 'U':
                    if(is_button(x, y - 1)) y--;
                    break;
                case 'R':
                    if(is_button(x + 1, y)) x++;
                    break;
                case 'D':
                    if(is_button(x, y + 1)) y++;
                    break;
                case 'L':
                    if(is_button(x - 1, y)) x--;
                    break;
            }
        }

        printf("%c", keypad[y + offset][x + offset]);
    
        line = strtok(NULL, delimiter);
    }

    // Free the allocated memory
    free(file_content);

    return 1;
}