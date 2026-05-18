from Module1_task.myapp.task_3 import BankAccount
import pytest
# def test_deposit():
#     user = BankAccount()
#     user.deposit(100)
#     assert user.balance == 100
#
# def test_withdraw():
#     user = BankAccount()
#     # assert user.withdraw(100) == 0
#     user.deposit(1000)
#     # assert user.withdraw(100) == 900
#     with pytest.raises(ValueError) as e:
#         user.withdraw(1100)
#     assert str(e.value) == "Insufficient funds"
#
# def test_fail_example():
#     user = BankAccount()
#     user.deposit(100)
#
#     result = {
#         "balance": user.balance,
#         "status": "active"
#     }
#
#     expected = {
#         "balance": 100,
#         "status": "active"
#     }
#
#     assert result == expected

class TestBankAccount:

    def setup_method(self):
        print(" ----setup_method")
        self.account = BankAccount()

    def teardown_method(self):
        print(" ---teardown_method")

    def test_deposit(self):
        self.account.deposit(100)
        assert self.account.balance == 100

    def test_withdraw(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        assert self.account.balance == 100

class TestIsolation:
    # def setup_method(self):
    #     self.account = BankAccount()

    def test_one(self):
        self.account = BankAccount()
        self.account.deposit(100)
        assert self.account.balance == 100

    def test_two(self):
        assert self.account.balance == 0