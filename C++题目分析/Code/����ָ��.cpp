#include<iostream>
#include<memory>
#include<string>
using namespace std;



class test
{
public:
	test(string s)
	{
		str = s; 
		cout << "test constructor running" << endl;
	}
	~test()
	{
		cout << "test delete running" << endl; 
	}
	string& getstr()
	{
		return  str; 
	}
	void setstr(string s)
	{
		str = s; 
	}
	void print()
	{
		cout <<"print="<< str << endl;
	}
private:
	string str; 
};

unique_ptr<test>fun()
{
	unique_ptr<test>temp(new test("hello  mike")); 
	return temp; 
}
int main()
{
	unique_ptr<test>ptest1(new test("123")); 
	unique_ptr<test>ptest2(new test("456"));
	ptest1->print();
	ptest2 = move(ptest1); 
	ptest2->print(); 
	if (ptest1 == NULL)
	{
		cout << "ptest1==NULL is true" << endl;
	}
	test *p = ptest2.release(); 
	p->print(); 
	ptest1.reset(p);
	ptest1->print();
	ptest2 = fun(); 
	ptest2->print();
	return   0;
	
}