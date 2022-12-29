#include <bits/stdc++.h>
#include <string>
 
using namespace std;
 
class Solution {
public:
    string sortSentence(string s) {
        vector<string> list(9);
        string word = "";
        string res = "";
        int index;
        int words = 0;
        for(int i=0;i<s.length();i++) {
            word += s[i];
            if(i+2 == s.length() || s[i+2] == ' ') {
                index = s[i+1] - '1';
                list[index] = word;
                word = "";
                words++;
                i += 2;
            }
        }
        
        for(int i=0;i<words;i++) {
            string str = list[i];
            res += str + (i == words-1 ? "" : " ");
        }
        return res;
    }
};
