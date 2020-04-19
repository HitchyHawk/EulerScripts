#include <iostream>
#include <cmath>
using namespace std;

int main() {
	//int list[6965];
	int const listMAX = 7181;
	int list[listMAX];
	int counter = 0;
	int MAX = 28123;
	MAX = 29000;
	int buffer;
	int sum = 0;
	float rooti;

	bool tg;

	//goes through all numbers under MAX
	for (int i = 1; i <= MAX; i++) {
		buffer = 0;
		rooti = pow(i, 0.5f);

		//Looks for divisors and adds to a buffer
		for (int divisor = 1; divisor <= rooti; divisor++) {

			if (i%divisor == 0) buffer += divisor + i / divisor;
		}
		buffer -= i;
		if (rooti == floor(rooti)) buffer -= rooti;

		/*
		if (rooti == floor(rooti)){

			for (int divisor = 1; divisor <= rooti; divisor++) {
	
				if (i%divisor == 0) buffer += divisor + i / divisor;
			}
			buffer -= rooti;
		}
		else {

			for (int divisor = 1; divisor < rooti; divisor++) {

				if (i%divisor == 0) buffer += divisor + i / divisor;
			}
		}
		buffer -= i;
		*/

		//if buffer is BLANK i, do thing
		if (buffer > i) {
			if (counter >= listMAX) cout << counter << endl;
			list[counter] = i;
			counter++;
			//cout << counter << endl;
			//cout << endl << i << endl;
		}
		
		tg = true;
		for (int x = counter; x >= 0; x--) {

			if (tg == false) break;

			for (int y = 0; y <= x; y++) {

				if (i - list[y] == list[x]) {

					tg = false;
					break;
				}
			}
		}

		if (tg == true) {
			sum += i;
		}

	}
	
	cout << "\nsum: " << counter  << " " << sum << endl;


	system("PAUSE");
	return 0;
}