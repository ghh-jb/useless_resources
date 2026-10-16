#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void unslid(const char *hx, int slide) {
	int len = strlen(hx);
	char dec[len + 1];
	for (int i = 0; i < len; i++) {
		char ptr = hx[i];
		if (ptr >= 'a' && ptr <= 'z') {
			dec[i] = (ptr - 'a' - slide + 26) % 26 + 'a';
		} else {
			dec[i] = ptr;
		}
	}
	dec[len] = '\0';
	printf("%s", dec);
}

int main(int argc, char *argv[]) {
	const char *hx = argv[1];
	int slide = atoi(argv[2]);
	unslid(hx, slide);
	return 0;
}

/*
Usage:
slider "Hryyb_jbeyq!" 13
Hello_world!
*/
