#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int top = -1;
char stk[100];

void push(char ele)
{
    stk[++top] = ele;
}

int pop()
{
    return stk[top--];
}

int priority(char ch)
{
    switch (ch)
    {
    case '(':
        return 1;
        break;
    case '-':
    case '+':
        return 2;
        break;
    case '/':
    case '':
        return 3;
        break;
    }
}
void get_postfix(charinf, char postf)
{
    char ch;
    ch = inf;
    int p = 0;
    while (ch != '\0')
    {
        if (isalpha(ch))
            postf[p++] = ch;
        else if (ch == '^' || ch == '(')
            push(ch);

        else if (ch == ')')
        {
            while (stk[top] != '(')
            {
                postf[p++] = pop();
            }
        }
        else
        {
            while (priority(stk[top]) >= priority(ch))
            {
                postf[p++] = pop();
            }
            push(*ch);
        }
        ch++;
    }
    while (top != -1) // pop from stack till empty
        postf[p++] = pop();
}
int postfix_eval(char pfx)
{
    char ch;
    int a,b;                        // operands
    int i=0;

    while((ch = pfx[i++]) != 0)
    {
        if(isalpha(ch))
        {
            int value;
            printf("Enter value of variable %c ", ch);
            scanf("%d", &value);
            push(value);
        }
        else                                // ch is an operator
        {
            b = pop();
            a = pop();
            double res;
            switch(ch)
            {
                case '+' : push(a + b); break;
                case '-' : push(a - b); break;
                case '' : push(a * b); break;
                case '/' : push(a / b); break;
                case '^' : res = pow(a, b);
                           push(res); break;
            }
        }
    }
    return stk[top];                            // returns result
}

void main()
{
    char inf[100], postf[100];
    printf("Please enter an infix expression without spaces\n");
    scanf("%s", &inf);
    get_postfix(inf, postf);
    printf("Infix expression: %s\n", inf);
    printf("Postfix expression: %s\n", postf);
    printf("Result after postfix evaluation is %d\n", postfix_eval(postf));
}
