#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define STACK_MX_SZ 64

#define ERR_STACK_OVERFLOW -2
#define ERR_STACK_UNDERFLOW -3

typedef struct stack{
    size_t size;
    int data[STACK_MX_SZ];
} stack_t;


void push(stack_t *stack, int val) {
    if (stack->size >= STACK_MX_SZ) {
        printf("FAULT: Stack overflow");
        exit(ERR_STACK_OVERFLOW);
    }
    stack->data[stack->size] = val;
    stack->size++;
}

int pop(stack_t *stack) {
    if (stack->size == 0) {
        printf("FAULT: Stack underlow");
        exit(ERR_STACK_UNDERFLOW);
    }
    stack->size--;
    return stack->data[stack->size];
}

int back(stack_t *stack) {
    if (stack->size <= 0) {
        exit(STACK_UNDERFLOW);
    }
    return stack->data[stack->size - 1];
}

int main(void) {
 	stack_t stack;
    stack.size = 0;
    push(&stack, 4);
}
