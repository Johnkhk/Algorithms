using namespace std;

#include <iostream>
#include <vector>
int main() {
    // std::cout << "Hello World!";
    // int i = -2;
    // cout<< i%26;
    cout<< "HEY" << endl;
    int n = 10;
    vector<int> a(n);
    vector<int> b(n);
    for (auto &key : a) key = rand()%10;
    for (auto key : b) key = rand()%10;
    for (int i = 0; i < n; i++) cout << a[i];
    cout << endl;
    for (int i = 0; i < n; i++) cout << b[i];
    return 0;

}

