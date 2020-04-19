#include <iostream>
using namespace std;

int main() {
	int a, buffer, count , max;
	max = 10000000;
	count = 0;

	for (int i = 1; i < max; i++) {
		if (i % 100000 == 0) cout << "%" << 100 * i / max << endl;
		a = i;
		while (a != 1){
			buffer = 0;
			while (a != 0) {
				buffer += (a % 10)*(a % 10);
				a /= 10;
			}
			a = buffer;
			if (a == 89) {
				count++;
				break;
			}
		}
	}
	cout << count << endl;




	system("PAUSE");
	return 0;
}