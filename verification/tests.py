"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "X+Y": [
        {
            "input":[lambda x,y:x+y,lambda x,y:(x**2-y**2)/(x-y)],
            "answer":{"args": (1,3),"kwargs": {},"result": (4,'same')},
            "explanation":""
        }      
    ]
}
