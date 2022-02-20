from code_518_coin_change_2 import Solution

def test_example_1():
    s = Solution()
    amount = 5
    coins = [1,2,5]
    output = 4
    assert s.change(amount, coins) == output