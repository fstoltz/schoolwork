def adder(inc): #Function returning a function
    return lambda x : x + inc
######################################################
######################################################
def json_encode( data ):
    if isinstance( data, bool ):
        if data:
            return "true"
        return "false"
######################################################
######################################################
    elif isinstance( data, ( int, float ) ):
        return str( data )
######################################################
######################################################
    elif isinstance( data, str ):
        replacements = [   #List containing tuples that match characters with desired replacement,
            ("\n", "\\n"), #adding new / removing replacements are made easier since it's a list that
            ("\t", "\\t"), #stores the replacements, and therefore would be easy to change / remove
            ("\a", "\\a"), #desired replacements via for example a GUI environment and not have to make manual changes
            ("\f", "\\f"), #inside the code
            ("\r", "\\r"),
        ]
        def prepareString(char):
            for item in replacements:
                if (char == item[0]):
                    return item[1]
            return char

        ##### ---- Alternative 1, using map() ------- #####
        li = []
        li += map(prepareString, data)
        jsonStr = ''.join(li)
        ##### ---- Alternative 2, using for loop ---- #####
        """
        jsonStr = ""
        for char in data:
            jsonStr += prepareString(char)
        """
        return '"' + jsonStr + '"'
######################################################
######################################################
    elif isinstance( data, list ):
        jsonStr = ""
        for x in data:
            jsonStr += json_encode(x) + ','  
        return '[' + jsonStr[:-1] + ']'
######################################################
######################################################
    elif isinstance( data, dict ):
        jsonStr = "" #Define empty string
        for key in data: #Iterate over the dictionary keys
            jsonStr += json_encode(key) + ':' + json_encode(data.get(key)) + ',' #Add the key, then the value to the jsonStr
        return '{' + jsonStr[:-1] + '}' #Return the JSON String without last comma
######################################################
######################################################
    elif isinstance( data, tuple ):
        jsonStr = ""
        for item in data:
            jsonStr +=  json_encode(item) + ','
        return '(' + jsonStr[:-1] + ')'
######################################################
######################################################
    else:
        # All other types do not  need to be implemented - it is OK that they raise an error
        raise TypeError( "%s is not JSON serializable" % repr( data ) )










