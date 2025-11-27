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

    unsigned int triangles[2000][3];

    unsigned char counter = 0;
    unsigned int nt = 0;    // Number of triangles
 
    // Read the triangles into the array
    // If the number of lines is not divideble by 3, the last 1 or 2 lines will be automaticly ignored
    while (line != NULL) {

        char *delimiter = "  ";
        char *part = strtok_r(line, delimiter, &part_pntr);
        
        unsigned int i = 0;
        while(i < 3) {
            triangles[nt + i][counter] = atoi(part);
            i++;
            
            part = strtok_r(NULL, delimiter, &part_pntr);
        }

        if(counter == 2) {
            counter = 0;
            nt+=3;
        } else {
            counter++;
        }
        
        line = strtok_r(NULL, l_delimiter, &line_pntr);
    }

    unsigned int possible_triangles = 0;

    // Iterate through the triangles
    for(int i = 0; i < nt; i++) {
        unsigned int *triangle = triangles[i];

        printf("%u %u %u", triangle[0], triangle[1], triangle[2]);

        if(triangle[0] + triangle[1] > triangle[2] && triangle[1] + triangle[2] > triangle[0] && triangle[0] + triangle[2] > triangle[1]) {
            printf("\tPossible");
            possible_triangles++;
        } 
        
        printf("\n");
    }

    printf("Number of possible triangles: %u", possible_triangles);

    // Free the allocated memory
    free(file_content);

    return 1;
}