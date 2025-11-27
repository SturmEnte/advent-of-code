#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../common/file_utils.h"

#define LOWERCASE_A 97
#define LOWERCASE_Z 122
#define ASCII_0     48
#define ASCII_9     57
#define O_BRACKET   91

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

    // Iterate through the instructions
    while (line != NULL) {
        
        // Letters a-z: 0=a 25=z
        char letter_usage[26] = {0};
        char checksum[6] = {0}; // length of checksum + 1 for \0
        char checksum_index = 0;
        short sector_id = 0;

        // Iterate through each character if the line
        for(int i = 0; line[i]; i++) {
            printf("%c", line[i]);

            // Letter
            if(line[i] >= LOWERCASE_A && line[i] <= LOWERCASE_Z) {

                if(checksum_index) {
                    checksum[checksum_index - 1] = line[i];
                    checksum_index++;
                    continue;
                }

                letter_usage[line[i] - LOWERCASE_A]++;

            } else if(line[i] >= ASCII_0 && line[i] <= ASCII_9 && !sector_id) { // If letter is a number and sector id is not set yet
                sector_id = (line[i] - ASCII_0) * 100 + (line[i+1] - ASCII_0) * 10 + (line[i+2] - ASCII_0);
            } else if(line[i] == O_BRACKET) {   
                checksum_index = 1;
            }
        }

        printf("\t| %s |\t%u\n", checksum, sector_id);

        line = strtok_r(NULL, l_delimiter, &line_pntr);
    }

    // Free the allocated memory
    free(file_content);

    return 1;
}