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
    
    char *l_delimiter = "\n";
    char *line_pntr, *part_pntr;
    char *line = strtok_r(file_content, l_delimiter, &line_pntr);

    unsigned int possible_triangles = 0;

    // Iterate through the instructions
    while (line != NULL) {

        char *delimiter = "  ";
        char *part = strtok_r(line, delimiter, &part_pntr);
        
        char i = 0;
        int sides[3]; 

        while(part != NULL) {
            printf("\"%s\" ", part);

            sides[i] = atoi(part);

            i++;
            part = strtok_r(NULL, delimiter, &part_pntr);
        }

        if(sides[0] + sides[1] > sides[2] && sides[1] + sides[2] > sides[0] && sides[0] + sides[2] > sides[1]) {
            printf("\tPossible");
            possible_triangles++;
        }   

        printf("\n");
        
        line = strtok_r(NULL, l_delimiter, &line_pntr);
    }

    printf("There are %d possible triangles in the input", possible_triangles);

    // Free the allocated memory
    free(file_content);

    return 1;
}