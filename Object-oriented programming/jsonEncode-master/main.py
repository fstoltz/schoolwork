import unittest
from myjson import json_encode, adder


class TestJsonEncode(unittest.TestCase):
    def test01_boolean_true( self ):
        self.assertEqual( json_encode( True ), "true" )

    def test02_boolean_false( self ):
        self.assertEqual( json_encode( False ), "false" )

    def test03_int( self ):
        self.assertEqual( json_encode( 1 ), "1" )

    def test04_float( self ):
        self.assertEqual( json_encode( 3.14159 ), "3.14159" )
        self.assertEqual( json_encode( 1.0/3.0 ), "0.3333333333333333" )

    def test05_string( self ):
        self.assertEqual( json_encode( "Hello World" ), '"Hello World"' )
        self.assertEqual( json_encode( "Buy\nmore\npizza" ), '"Buy\\nmore\\npizza"' )
        self.assertEqual( json_encode( "Mark's test" ), '"Mark\'s test"' )

    def test06_simple_list( self ):
        self.assertEqual( json_encode(  [True,False] ), "[true,false]" )

    def test07_mixed_list( self ):
        self.assertEqual( json_encode(  [False,3,3.14159,"Pi"] ), "[false,3,3.14159,\"Pi\"]" )


    def test08_simple_dict( self ):
        self.assertEqual( json_encode(  {"hello":"world"} ), '{"hello":"world"}' )

    def test09_mixed_dict( self ):
        self.assertEqual( json_encode(  {"name":"Mark", "age":12, "teacher":True} ), '{"name":"Mark","age":12,"teacher":true}' )

    def test10_complex_data( self ):
        complex_data = {
            "name": "Advanced Python Training",
            "date": "October 13, 2012",
            "completed": False,
            "instructor": {
                "name": "Anand Chitipothu",
                "website": "http://anandology.com/"
            },
            "participants": [
                {
                    "name": "Participant 1",
                    "email": "email1@example.com"
                },
                {
                    "name": "Participant 2",
                    "email": "email2@example.com"
                }
            ]
        }
        self.assertEqual( json_encode( complex_data ),
                          '{"name":"Advanced Python Training","date":"October 13, 2012","completed":false,"instructor":{"name":"Anand Chitipothu","website":"http://anandology.com/"},"participants":[{"name":"Participant 1","email":"email1@example.com"},{"name":"Participant 2","email":"email2@example.com"}]}' )
###################################################
#               My code starts here               #
###################################################
    def test11_list_with_dicts (self):
        
        data = [{"name":"Fredrik"}, 
                  {"name":"Peter"},
                  {"familyMembersAge": [3, 5, 8, 40, 42, 80, 85]}]

        self.assertEqual( json_encode( data ), '[{"name":"Fredrik"},{"name":"Peter"},{"familyMembersAge":[3,5,8,40,42,80,85]}]' )

    def test12_bunch_of_data (self):

        add4 = adder(4)

        data = [3.14,
                  5,
                  'Name is \a{name}, though people call me "{nickname}"'.format(name='Wicked', nickname="DaWick'd"),
                  True,
                  False,
                  60/2,
                  {"key1" : (25 + 25) / 2,
                   "key2" : "He" + "llo"},
                   [2, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9],
                   [1, [2, 3], [4, [5, 6, False/True, {"numb" : add4((5.5/5.5) + 1)}, str(5)]]]]

        data.append( (60, 70) )
        data.append("finalElement")

        self.assertEqual( json_encode( data ), '[3.14,5,"Name is \\aWicked, though people call me "DaWick\'d"",true,false,30.0,{"key1":25.0,"key2":"Hello"},[2,4,8,16,32,64,128,256,512],[1,[2,3],[4,[5,6,0.0,{"numb":6.0},"5"]]],(60,70),"finalElement"]' )

    def test13_basic_tuple( self ):

        data = (25, 50, "hi there 'cousin'!")

        self.assertEqual( json_encode(  data ), '(25,50,"hi there \'cousin\'!")' )

    def test14_complex_tuple( self ):
        #g = lambda x : x + 1
        data = (25, int(50/2), "ho'w'dy", True, ["start \"of\" list", 1, 2, [5, 10]], {"name" : [1337**2]})

        self.assertEqual( json_encode(  data ), '(25,25,"ho\'w\'dy",true,["start "of" list",1,2,[5,10]],{"name":[1787569]})' )

    def test15_string_with_mixed_quotes( self ):
        data = "hejsan \"jag\" heter 'iv'r'ig', vad \"he't'er\" du?"


        self.assertEqual( json_encode( data ), '"hejsan "jag" heter \'iv\'r\'ig\', vad "he\'t\'er" du?"' )


if __name__ == '__main__':
    unittest.main(verbosity=2)
