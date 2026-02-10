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
	printf("4. Add user in wheel group\n");
	printf("5. Delete already added user\n");
	printf("6. (...) More to be added?\n");
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
		system("http_proxy= https_proxy= ftp_proxy= setsid firefox");
		printf("firefox shoud be starting, exiting\n");
		exit(0);
	}
	else if (ch == 4) {
		int ret = setuid(0);
		printf("ret: %i\n", ret);
		system("/usr/sbin/useradd -N -M work");
		system("/usr/sbin/usermod -aG wheel work");
		printf("system user {work} created");
		printf("Setting password: {password}\n");
		system("echo 'work:password' | /usr/sbin/chpasswd");
		printf("{work} user password: {password}\n");
		printf("try to enter via tty3\n");
		// DONE: Add automatic password setting
		return 0;
	}
	else if (ch == 5) {
		int ret = setuid(0);
		printf("ret: %i\n", ret);
		system("/usr/sbin/userdel work");
		system("rm -rf /var/spool/mail/work");
		// system("rm -rf /home/work"); // I do not create home directory by default
		printf("deleted system user: {work}; removed mail\n");
		return 0;
	}
	else {
		printf("error\n");
		return -1;
	}
	return 0;
}
