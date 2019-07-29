/*
#include<iostream>
#include<vector>
using namespace std; 
template<class T>
class  A
{   public:
	A(T temp)
	{
		cout << "A construct " << endl; 
		print_r = temp; 
	}
	bool te(const T&t1, const T  &t2); 
    private:
		T print_r;
};
template<class T>
bool  A<T>::te(const T&t1, const T  &t2)
{
	if (t1 == t2)
	{
		return  true; 

	}
	else
	{
		return false; 
	}
}

int main()
{

	A<int>a(1); 
	if (a.te(2, 3))
	{
		cout << "no  no no no " << endl;
	}
	else
	{
		cout << "yes yes " << endl; 
	}
	
	return 1; 
}*/

#include<iostream>
using namespace std; 
template<class T>
class A
{
public:
	A(T par); 
	bool iseq(T par1, T par2); 
private:
	T p;
};
template<class T>
A<T>::A(T par)
{
	this->p = par; 
}
template<class T>
bool A<T>::iseq(T par1, T par2)
{
	if (par1 == par2)
	{
		cout << "yes " << endl; 
		return true;
	}
	else
	{
		cout << "no" << endl; 
		return false; 
	}
  
}
int main()
{
	A<int> t1(10);
	return 0; 

}