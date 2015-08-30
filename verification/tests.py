"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "$5.34",
            "answer": "$5.34"
        },
        {
            "input": "$5,34",
            "answer": "$5.34"
        },
        {
            "input": "$222,100,455.34",
            "answer": "$222,100,455.34"
        },
        {
            "input": "$222.100.455,34",
            "answer": "$222,100,455.34"
        }, 
        {
            "input": "$222,100,455",
            "answer": "$222,100,455"
        }, 
        {
            "input": "$222.100.455",
            "answer": "$222,100,455"
        }          
    ],
    "Extra": [
        {
            "input": "$4,13 + $5,24 = $9,37",
            "answer": "$4.13 + $5.24 = $9.37"
        },
        {
            "input": "$4,13 + $1.005,24 = $1.009,37",
            "answer": "$4.13 + $1,005.24 = $1,009.37"
        },
        {
            "input": "$8.000 - $8.000 = $0",
            "answer": "$8,000 - $8,000 = $0"
        },
        {
            "input": "$4.545,45 is less than $5,454.54.",
            "answer": "$4,545.45 is less than $5,454.54."
        },
        {
            "input": "$4,545.45 is less than $5.454,54.",
            "answer": "$4,545.45 is less than $5,454.54."
        },
        {
            "input": "Our movie tickets cost $12,20.",
            "answer": "Our movie tickets cost $12.20."
        },     
        {
            "input": "127.255.255.255",
            "answer": "127.255.255.255"
        },
        {
            "input": ("Clayton Kershaw $31.000.000\n"
                    "Zack Greinke   $27.000.000\n"
                    "Adrian Gonzalez $21.857.143\n"),
            "answer": ("Clayton Kershaw $31,000,000\n"
                    "Zack Greinke   $27,000,000\n"
                    "Adrian Gonzalez $21,857,143\n")
        }        
    ]
}
