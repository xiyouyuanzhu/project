#include<iostream>
#include<string.h>
#include<string>
#include<vector>
using namespace std; 
int strReverse()
{
	char str[1024]; 
	cin.getline(str,1024);
	int len = strlen(str); 
	char *target = (char*)malloc((len + 1)*sizeof(char)); 
	for (int i = 0; i < len; i++)
	{
		target[i] = str[len - 1 - i]; 
	}
	target[len] = '\0'; 
	cout << "target  = " << target << endl;
	return 0; 
}
void newline()
{
	char  ans; 
	do
	{
		ans = getchar();
	} while (ans != '\n'); 
}
int BignumMulti()
{
	char ans = 'y'; 
	while (ans == 'y'||ans=='Y')
	{

		string n1 = "";
		string n2 = "";
		cout << "Input n1" << endl;
		getline(cin, n1);
		cout << "Input n2" << endl;
		getline(cin, n2);
		int len1 = n1.size();
		int len2 = n2.size();
		string  lstr = "";
		string sstr = "";
		(len1 > len2) ? (lstr = n1, sstr = n2) : (lstr = n2, sstr = n1);
		//cout << "lstr=" << lstr << endl;
		//cout << "sstr = " << sstr << endl;
		string  target = string((len1 + len2), '0');
		//cout << "strTarget=" << strTarget << endl;

		int multi = 1;
		for (int i = (lstr.size() - 1); i >= 0; i--)
		{

			int carry = 0;
			for (int j = sstr.size() - 1; j >= 0; j--)
			{
				multi = (lstr[i] - '0')*(sstr[j] - '0') + (target[i + j + 1] - '0') + carry;
				int s = multi / 10;
				int y = multi % 10;
				target[i + j + 1] = y + '0';
				carry = s;
			}
			if (carry > 0)
			{
				cout << "target[i]=" << target[i] << endl;
				target[i] = carry + '0';
			}
		}
		string targetpro = "";
		for (int i = 0; i < target.size(); i++)
		{
			if (target[i] != '0')
			{
				for (int j = i; j < target.size(); j++)
				{

					targetpro += target[j];
				}
				break;
			}
		}
		cout << "target= " << targetpro << endl;
		cout << "Enter y or Y to try again" << endl; 
		newline(); 

		ans = getchar(); 
		
	
	}
	return  0; 

}
int t1()
{
	for (int i = 0; i < 10; i--)
	{
		cout << i << endl; 
	}
	return  0;
}
int main()
{
	BignumMulti(); 
	//t1();
	return   0; 
}
