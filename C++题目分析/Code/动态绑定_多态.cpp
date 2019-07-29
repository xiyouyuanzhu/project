#include<iostream>
using namespace std; 
class base
{
public:
	void do_something(); 
	virtual void do_other(); 
private:

};
void base:: do_something()
{
	cout << "base ::do_something" << endl; 
}
void base::do_other()
{

}
class son1:public base
{
public:
	void do_something(); 
	virtual void do_other(); 
private:

};
void  son1::do_something()
{
	cout << "son1 do_something" << endl; 
}
void  son1::do_other()
{
	cout << "son1 do_other" << endl;
}

void main()
{

	base * b = new son1; 
	b->do_something(); 
	b->do_other(); 

}