#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdarg.h>

void printf_success(char* format, ...) {
    printf("\x1b[1;32m");
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    printf("\x1b[0m");
    return;
}

void show_usage() {
	printf("=== Management utility ===\n");
	printf_success("Usage:\n");
	printf("1. Exec /bin/bash with root privileges\n");
	printf("2. Unblock iptables OUTPUT restrictions\n");
	printf("3. Start unlocked firefox\n");
	printf("4. (...) More to be added?\n");
	printf("write your suggestions to /.flag.txt\n");
	return;
}

int main(int argc, char const *argv[])
{
	show_usage();
	int ch = 0;
	scanf("%i", &ch);
	if (ch == 0) {
		printf("error\n");
		return -1;
	}
	else if (ch == 1) {
		int ret = setuid(0);
		printf("ret: %i\n", ret);
		execve("/bin/bash", NULL, NULL);
	}
	else if (ch == 2) {
		int ret = setuid(0);
		printf("ret: %i\n", ret);
		system("/usr/sbin/iptables -P OUTPUT ACCEPT");
		system("systemctl restart iptables.service");
		printf_success("send operation: allowed\n");
		return 0;
	}
	else if (ch == 3) {
		system("setsid firefox");
		printf("firefox shoud be starting, exiting\n");
		return 0;
	}
	else {
		printf("error\n");
		return -1;
	}
	return 0;
}
