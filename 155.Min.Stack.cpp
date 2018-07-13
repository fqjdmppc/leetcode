class MinStack {
public:
    /** initialize your data structure here. */
    typedef struct NODE
    {
        int val;
        int current_min;
        struct NODE* father;
    } node;
    
    node* last;
    
    MinStack() {
        last = NULL;
    }
    
    void push(int x) 
    {
        node *temp = new node;
        temp->val = x;
        temp->father = last;
        if (last != NULL)
        {
            temp->current_min = min(temp->val, last->current_min);
        }
        else temp->current_min = temp->val;
        last = temp;
    }
    
    void pop() {
        node* temp = last;
        last = last->father;
        delete temp;
    }
    
    int top() {
        return last->val;
    }
    
    int getMin() {
        return last->current_min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */