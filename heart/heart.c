#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#define X 200
#define Y 100

int points[X*Y][2];


int get_x(double t) {
	return 50.0*sqrt(2)*pow(sin(t), 3);
}

int get_y(double t) {
	return 25.0*(- pow(cos(t), 3) - pow(cos(t), 2) + 2 * cos(t));
}

int numulate(int index) {
	return (Y - points[index][1]) * X + (X + points[index][0]);
}

void swap(int a, int b) {
	points[a][0] += points[b][0];
	points[b][0] = points[a][0] - points[b][0];
	points[a][0] -= points[b][0];

	points[a][1] += points[b][1];
	points[b][1] = points[a][1] - points[b][1];
	points[a][1] -= points[b][1];
}

void shift(int i, int f) {
	for (int j = i; j < sizeof(points)/sizeof(points[0]); j++) {
		points[j - i + f][0] = points[j][0];
		points[j - i + f][1] = points[j][1];
	}
}

void rem_dups() {
	int inx = points[0][0];
	int iny = points[0][1];
	int index = 0;
	for (int i = 1; i < sizeof(points)/sizeof(points[0]); i++) {
		if (points[i][0] == inx && points[i][1] == iny) {

		} else {
			if (i - index > 1) {
				shift(i, index);
				i -= i - index;
			}
			inx = points[i][0];
			iny = points[i][1];
			index = i;
		}
	}
}

void srt() {
	for (int j = 0; j < sizeof(points)/sizeof(points[0]) - 1; j++) {
		for (int i = 0; i < sizeof(points)/sizeof(points[0]) - 1; i++) {
			// if (numulate(i) > numulate(i + 1)) {
			// 	swap(i, i + 1);
			// }
			if (points[i][1] < points[i + 1][1]) {
				swap(i, i + 1);
			}
			if (points[i][1] == points[i + 1][1] && points[i][0] > points[i + 1][0]) {
				swap(i, i + 1);
			}
		}
	}
}

int display() {
	int index = 0;
	for (int y = Y/2; y > -Y/2; y--) {
		for (int x = -X/2; x < X/2; x++) {
			// printf("%d:%d", x, y);
			if (points[index][0] == x && points[index][1] == y) {
				printf("*");
				index++;
			} else {
				printf(" ");
			}
		}
		printf("\n");
	}
}

int main() {
	int counter = 0;
	int holder[2];
	for (double i = 0.0; i > -7.0; i -= 0.01) {
		points[counter++][0] = get_x(i);
		points[counter - 1][1] = get_y(i);
		// printf("%d ", counter - 1);
		// holder[0] = points[counter - 1][0];
		// holder[1] = points[counter - 1][1];
		// // printf("%d %d:", holder[0], holder[1]);
		// if (holder[0] != 0) {
		// 	for (int j = holder[0] - holder[0]/abs(holder[0]); ((holder[0] < 0) ? (j <= 0) : (j >= 0)); j -= holder[0]/abs(holder[0])) {
		// 		points[counter++][0] = j;
		// 		// printf("%d ", j);
		// 		points[counter - 1][1] = holder[1];
		// 		printf("%d ", counter - 1);
		// 	}
		// 	printf("\n");
		// }
	}
	srt();
	rem_dups();
	// for (int i = 0; i < 100; i++) {
	// 	printf("%d %d\n", points[i][0], points[i][1]);
	// }

	display();

	return 0;
}