#include<stack>
#include<iostream>
using namespace std; 

void testOstack()
{
	stack<int>mystack; 
	for (int i = 0; i < 10;i++)
	{
		cout << i << '\t'; 
		mystack.push(i); 
	}
	cout << endl; 
	int size = mystack.size(); 
	cout << "size= " << size << endl; 
	for (int i = 0; i < size; i++)
	{
		cout << mystack.top() << '\t'; 
		mystack.pop(); 
	}
}




// 数组实现的栈
#define MAX 100
class arrayStack
{
public:
	void push(int n)
	{
		arr[lenth++] = n;
	}
	void pop()
	{
		lenth--;
	}
	int top()
	{
		return arr[lenth - 1]; 
	}
	int size()
	{
		return lenth; 
	}
	bool isempty()
	{
		if (lenth <= 0)
		{
			return true;
		}
		else
		{
			return false; 
		}
	}
	
private:
	int lenth=0; 
	int arr[MAX]; 
};
void testAstack()
{

	arrayStack  sta; 
	arrayStack  sta1; 
	int t[] = { 10, 20, 30, 40 }; 
	for (int i = 0; i < 4;  i++)
	{ 
		cout << t[i] << "\t"; 
		sta.push(t[i]); 
	}
	cout << endl; 
	cout << "sta.size()=" << sta.size() << endl;
	while (!sta.isempty())
	{
		cout << sta.top() << "\t";
		sta.pop();
	}
	
}

struct node
{
		
		int data = 0;
		node * link;
	
};
typedef  node* nodeptr; 
class struStack
{

public:
	struStack()
	{
		head = new node();
		top = new node();
		head = NULL; 
	}
	void push(int n)
	{
		nodeptr newnode = new node();
		newnode->data = n;
		if (lenth == 0)
		{
			newnode->link = head;
		}
		else
		{
			newnode->link = top;
		}
		top = newnode;
		lenth++;
	}
	void pop()
	{
		if (lenth <= 0)
		{
			cout << "pop error" << endl;
			exit(1);
		}
		else
		{
			nodeptr dlt = new node();
			dlt = top;
			int data = dlt->data;
			top = top->link;
			delete dlt;
			lenth--;
		}
	}
	int topdata()
	{
		int data = top->data;
		return data;
	}
	int size()
	{
		return lenth; 
	}
	bool isempty()
	{
		if (lenth <= 0)
		{
			return true; 
		}
		return false;
	}
	void dltAll()
	{
		while (!isempty())
		{
			//pop();
			if (top->link != NULL)
			{
				nodeptr dlt = new node();
				dlt = top;
				top = top->link;
				delete dlt;
				lenth--;
			}
			else
			{
				delete top;
				lenth--;
			}
		}
	}
	int findMax()
	{
		int max = topdata();
		nodeptr  tempstr = new node; 
		tempstr = top; 
		for (int i = 0; i < lenth;i++)
		{
			int tempdata = tempstr->data; 
			if (max < tempdata)
			{
				max = tempdata; 
			}
			else
			{
				continue; 
			}
			tempstr = tempstr->link;
		}
		return max; 
	}

private:
	nodeptr head; 
	nodeptr top; 
	int lenth=0; 
};
	
void testSturStack()
{
	struStack sta;
	int t[] = { 10, 20, 30, 40 };
	for (int i = 0; i < 4; i++)
	{
		cout << t[i] << "\t";
		sta.push(t[i]);
	}
	cout << endl;
	cout << "sta.size()=" << sta.size() << endl;
	int target =sta.findMax();
	cout << "target max =" << target << endl; 
	cout << "sta.size() = "<<sta.size() << endl; 

}
int main()
{

	testSturStack();

	return 0; 

}