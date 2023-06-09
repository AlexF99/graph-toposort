#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string inp;
    ifstream MyReadFile("graph0.dot");
    while (getline(MyReadFile, inp))
    {
        if (inp.find('{') == std::string::npos && inp.find('}') == std::string::npos)
        {
            remove(inp.begin(), inp.end(), ' ');
            inp.resize(inp.find(';'));
            cout << inp << endl;
        }
    }

    MyReadFile.close();
    return 0;
}