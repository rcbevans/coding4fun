#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <sstream>

#define N 1000000000000000000

#define ZERO 0
#define ONE 1
#define TWO 2

using namespace std;

std::vector<std::string> powers_of_11(){
	stringstream ss;
	string str = "";
	std::vector<std::string> map(18);
	for (int i = 1; i <= 18; i++){
		ss.str(std::string());
		ss << pow(11, i);
		map[i-1] = ss.str();
	}
	return map;
}

 double string_to_double( const std::string& s )
 {
   std::istringstream i(s);
   double x;
   if (!(i >> x))
     return 0;
   return x;
 } 

int main(){
	std::vector<std::string> powers = powers_of_11();
	unsigned long long int count = ZERO;
	unsigned long long int candidate = ONE;
	unsigned long long int strlength;
	stringstream ss;
	string str = "";
	bool broken = false;
	int i,j;
	while(count < N){
		ss.str(std::string());
		ss << candidate;
		str = ss.str();
		broken = false;
		strlength = str.length();
		if (strlength > TWO) {
			for (i = strlength; i >= TWO; i--){
				for (j = ZERO; j <= strlength - i; j++){
					if ((str[j+i-ONE] == '1') && (str.substr(j, i) == powers[i-TWO]))
							goto bypass;
				}
			}
			count++;	
		}
		else if (str != powers[ZERO]){
			count++;
		}
		bypass:
		candidate++;
	}
	cout << "Result is: " << candidate - ONE << endl;
}