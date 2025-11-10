#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define STACK_MX_SZ 64

#define ERR_STACK_OVERFLOW -2
#define ERR_STACK_UNDERFLOW -3
#define ERR_NOERR 0

typedef struct stack {
    size_t size;
    int top;
    int data[STACK_MX_SZ];
} stack_t;


int back(stack_t *stack) {
    if (stack->size <= 0) {
        printf("FAULT: Stack underlow");
        exit(ERR_STACK_UNDERFLOW);
    }
    return stack->data[stack->size - 1];
}

void push(stack_t *stack, int val) {
    if (stack->size >= STACK_MX_SZ) {
        printf("FAULT: Stack overflow");
        exit(ERR_STACK_OVERFLOW);
    }
    stack->data[stack->size] = val;
    stack->size++;
    stack->top = back(stack);
}

int pop(stack_t *stack) {
    if (stack->size == 0) {
        printf("FAULT: Stack underlow");
        exit(ERR_STACK_UNDERFLOW);
    }
    stack->size--;
    stack->top = back(stack);
    return stack->data[stack->size];
}

int size(stack_t *stack) {
    if (stack->size <= 0) {
        printf("FAULT: Stack underlow");
        exit(ERR_STACK_UNDERFLOW);
    }
    return stack->size;
}

void clear(stack_t *stack) {
    stack->size = 0;
    stack->top = 0;
    memset((void*)(stack), 0x0, sizeof(stack));
    printf("ok");
    return;
}

void my_exit() {
    printf("bye");
    exit(ERR_NOERR);
}

void printStack(stack_t *stack) {
    int i;
    int len = stack->size - 1;
    printf("stack size %d > ", stack->size);
    for (i = 0; i < len; i++) {
        printf("%i", stack->data[i]);
        printf(" | ");
    }
    if (stack->size != 0) {
        printf("%i", stack->data[i]);
    }
    printf("\n");
}

int main(void) {
 	stack_t stack;
    stack.size = 0;
    push(&stack, 4);
    push(&stack, 5);
    push(&stack, 6);
    push(&stack, 7);
    push(&stack, 8);

    printStack(&stack);

    clear(&stack);
    printStack(&stack);

}
