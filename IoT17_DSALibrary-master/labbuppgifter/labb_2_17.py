
from stack import LLStack

def hasBalancedParenthesis( s ):
    stack=LLStack()
    for c in s:
        if c == "(" or c == "[":
            stack.push(c)
        elif c == ")" or c == "]":
            mc = stack.pop()
            if mc == "(" and c != ")":
                return False
            if mc == "[" and c != "]":
                return False
    return True


print( hasBalancedParenthesis( "(())" ) )  # True
print( hasBalancedParenthesis( "([])" ) )  # True
print( hasBalancedParenthesis( "([)]" ) )  # False
print( hasBalancedParenthesis( "Hej ( pa [ dig ] vad ) heter ( [ du ] )?" ) )  # True

