import unittest
import Owner
import tkinter

class MyTest(unittest.TestCase):

    def test_check_penalty_true(self):

        diction = {'y_amount': 20, 'a_amount': 10, 'o_amount': 5, 
                   'young_cost': 300, 'adult_cost': 200, 'old_cost': 100,
                   'young_sell': 350, 'adult_sell': 250, 'old_sell': 150,
                   'capital': 50000, 'all_food': 15000, 'penalty': 50}

        owner = Owner.Owner(diction, year=3)

        self.assertEqual(owner.check_penalty(), 35750)

    def test_check_penalty_false(self):

        diction = {'y_amount': 20, 'a_amount': 10, 'o_amount': 5, 
                   'young_cost': 300, 'adult_cost': 200, 'old_cost': 100,
                   'young_sell': 350, 'adult_sell': 250, 'old_sell': 150,
                   'capital': 50000, 'all_food': 15000, 'penalty': 50}

        owner = Owner.Owner(diction, year=3)

        if owner.check_penalty() != 30:
            flag = True
        else:
            flag = False

        self.assertEqual(flag, True)

    def test_sell_true(self):

        diction = {'y_amount': 20, 'a_amount': 10, 'o_amount': 5, 
                   'young_cost': 300, 'adult_cost': 200, 'old_cost': 100,
                   'young_sell': 350, 'adult_sell': 250, 'old_sell': 150,
                   'capital': 50000, 'all_food': 15000, 'penalty': 50}

        owner = Owner.Owner(diction, year=3)

        self.assertEqual(owner.sell(), 177750)

    def test_sell_false(self):

        diction = {'y_amount': 20, 'a_amount': 10, 'o_amount': 5, 
                   'young_cost': 300, 'adult_cost': 200, 'old_cost': 100,
                   'young_sell': 350, 'adult_sell': 250, 'old_sell': 150,
                   'capital': 50000, 'all_food': 15000, 'penalty': 50}

        owner = Owner.Owner(diction, year=3)

        if owner.check_penalty() != 177750:
            flag = True
        else:
            flag = False

        self.assertEqual(flag, True)

    def test_paying_capacity_true(self):

        diction = {'y_amount': 20, 'a_amount': 10, 'o_amount': 5, 
                   'young_cost': 300, 'adult_cost': 200, 'old_cost': 100,
                   'young_sell': 350, 'adult_sell': 250, 'old_sell': 150,
                   'capital': 50000, 'all_food': 15000, 'penalty': 50}

        owner = Owner.Owner(diction, year=3)

        self.assertEqual(owner.paying_capacity(), False)

if __name__ == '__main__':
    unittest.main()