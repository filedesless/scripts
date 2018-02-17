#include <iostream>
#include <string>
#include <map>
#include <vector>

/* - idea and original code from epoch -
 aggregates lines from stdin with the
 same first identifier before a given delimiter

 usage: clump [delim]
*/

int main(int argc, char** argv) {
	using namespace std;
	string delim(" ");
	map<string, vector<string>> dict;

	if (argc > 1)
		delim = argv[1];

	for (string line; getline(cin, line);) {
		int n = line.find(delim);
		if (n != string::npos) {
			string id(line.substr(0, n)),
				rest(line.substr(n + 1, line.size()));
			dict[id].push_back(rest);
		}
	}

	for (auto& kv : dict) {
		cout << kv.first;
		for (auto& item : kv.second)
			cout << delim << item;
		cout << endl;
	}

	return 0;
}
