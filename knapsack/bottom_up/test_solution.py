from solution import solution


def tests():
    tests = [
        {
            "name": "Test Case 1",
            "args": {
                "profit": [],
                "weight": [],
                "capacity": 0
            },
            "want": 0,
        },
        {
            "name": "Test Case 2",
            "args": {
                "profit": [1],
                "weight": [1],
                "capacity": 0
            },
            "want": 0,
        },
        {
            "name": "Test Case 3",
            "args": {
                "profit": [1],
                "weight": [1],
                "capacity": 1
            },
            "want": 1,
        },
        {
            "name": "Test Case 4",
            "args": {
                "profit": [1, 2],
                "weight": [1, 1],
                "capacity": 1
            },
            "want": 2,
        },
        {
            "name": "Test Case 5",
            "args": {
                "profit": [1, 2, 2],
                "weight": [1, 1, 1],
                "capacity": 2
            },
            "want": 4,
        },
        {
            "name": "Test Case 6",
            "args": {
                "profit": [1, 1, 3],
                "weight": [1, 1, 2],
                "capacity": 2
            },
            "want": 3,
        },
        {
            "name": "Test Case 7",
            "args": {
                "profit": [1, 2],
                "weight": [1, 3],
                "capacity": 2
            },
            "want": 1,
        },
        {
            "name": "Test Case 7",
            "args": {
                "profit": [1, 2],
                "weight": [1, 3],
                "capacity": 2
            },
            "want": 1,
        },
    ]

    for test in tests:
        got = solution(**test["args"])

        if test['want'] != got:
            raise Exception(f"{test['name']}, expected {test['want']}, recieved {got}")
