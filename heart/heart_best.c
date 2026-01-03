#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#define X 80*2.62
#define Y 20*3
#define K 99.75
#define f 0.1


void slp(int t) {
	struct timespec remaining, request = {0, t};
	int response = nanosleep(&request, &remaining);
}

int main() {
	system("clear");
	for (double i = 0; i < 0.3; i+= 0.01) {
		for (int y = Y/2; y > -Y/2; y--) {
			for (int x = -X/2; x < X/2; x++) {
				if (pow((pow(i*x, 2)+pow(2*i*y, 2)-1), 3) <= pow(i*x, 2)*pow(2*i*y, 3)) {
					printf("*");
				} else {
					printf(" ");
				}
			}
			printf("\n");
		}
		slp(50000000);
		system("clear");
	}
	for (double i = 0.3; i > 0; i-= 0.01) {
		for (int y = Y/2; y > -Y/2; y--) {
			for (int x = -X/2; x < X/2; x++) {
				if (pow((pow(i*x, 2)+pow(2*i*y, 2)-1), 3) <= pow(i*x, 2)*pow(2*i*y, 3)) {
					printf("*");
				} else {
					printf(" ");
				}
			}
			printf("\n");
		}
		slp(50000000);
		system("clear");
	}

	return 0;
}