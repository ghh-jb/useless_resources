#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hexToAscii(const char *hex) {
	int len = strlen(hex);
	char ascii[len / 2 + 1];
	ascii[len / 2] = '\0';

	for (int i = 0; i < len; i += 2) {
		char byte[3] = { hex[i], hex[i + 1], '\0' };
		ascii[i / 2] = (char)strtol(byte, NULL, 16);
	}
	printf("%s", ascii);
}

int main(int argc, char *argv[]) {
	const char *hx = argv[1];
	hexToAscii(hx);
	return 0;
}

/* 
Usage:
hexdamp 48656c6c6f20776f726c6421
Hello world!
*/
