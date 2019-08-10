#include<iostream>
#include<string>
using namespace std;
//Ç³¿½±´
class String
{
public:
	String(char *str) :_str(_str = new char[strlen(str)+1])
	{
		strcpy(_str, str);
	}
	String(const String&s) :_str(s._str)
	{ 
		
	}
	String& operator=(const String&s)
	{
		if (this != &s)
		{
			_str = s._str; 
		}
		return *this; 
	}
	~String()
	{
		if (_str)
		{
			delete[]_str; 
		}
		_str = NULL;
	
	}

private:
	char *_str; 


};

//Éî¿½±´
class String
{
public:
	String(char *str) :_str(_str = new char[strlen(str) + 1])
	{
		strcpy(_str, str);
	}
	String(const String&s) 
	{
		this->_str = new char(strlen(s._str) + 1); 
		strcpy(_str, s._str);
	}
	String& operator=(const String&s)
	{
		if (this != &s)
		{
			this->_str = new char(strlen(s._str) + 1); 
			strcpy(this->_str, s._str);
		}
		return *this;
	}
	~String()
	{
		if (_str)
		{
			delete[]_str;
		}
		_str = NULL;

	}

private:
	char *_str;


};
int main()
{


	return 0; 
}