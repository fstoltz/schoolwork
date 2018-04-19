
from stack import LLStack

def reverse_polish_eval( s ):
    stack=LLStack()
    commands=s.split(" ")
    for cmd in commands:
        if cmd=="+":
            stack.push( stack.pop() + stack.pop() )
        elif cmd=="-":
            stack.push( stack.pop() - stack.pop() )
        elif cmd=="*":
            stack.push( stack.pop() * stack.pop() )
        elif cmd=="/":
            stack.push( stack.pop() / stack.pop() )
        else:
            stack.push( int( cmd ) )
    return stack.pop()

print( reverse_polish_eval( "5 9 3 + 4 2 * * 7 + *" ) )  # 515
print( reverse_polish_eval( "1000 990 1 2 + * +" ) )     # 3970
