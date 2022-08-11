from enum import Enum


class State(Enum):
    Q0 = 1
    Q1 = 2
    Q2 = 3
    QD = 4


# very elegant!!!
class StateMachine:
    def __init__(self) -> None:
        self.currentState = State.Q0
        self.INT_MAX = pow(2, 31) - 1
        self.INT_MIN = pow(2, 31)
        self.result = 0
        self.sign = 1

    def transit_to_q1(self, ch) -> None:
        if(ch == '-'):
            self.sign = -1
        self.currentState = State.Q1

    def transit_to_q2(self, digit: int) -> None:
        if (self.result > self.INT_MAX // 10) or (self.result == self.INT_MAX // 10 and digit > self.INT_MAX % 10):
            self.result = self.INT_MAX if self.sign == 1 else self.INT_MIN
            self.currentState = State.QD
        else:
            self.result = self.result * 10 + digit
            self.currentState = State.Q2

    def transition(self, ch: chr) -> None:
        if self.currentState == State.Q0:
            # the initial state
            if ch == ' ':
                return
            elif ch == '-' or ch == '+':
                self.transit_to_q1(ch)
            elif ch.isdigit():
                self.transit_to_q2(int(ch))
            else:
                self.currentState = State.QD
        elif self.currentState == State.Q1 or self.currentState == State.Q2:
            if ch.isdigit():
                self.transit_to_q2(int(ch))
            else:
                self.currentState = State.QD

    def get_result(self) -> int:
        return self.sign * self.result

    def get_current_state(self) -> State:
        return self.currentState


class Solution:
    def myAtoi(self, s: str) -> int:
        sm = StateMachine()
        for ch in s:
            sm.transition(ch)
            if sm.get_current_state() == State.QD:
                break
        return sm.get_result()
        # method 1
        # sign = 1
        # result = 0
        # index = 0
        # n = len(s)

        # INT_MAX = pow(2, 31) - 1
        # INT_MIN = -pow(2, 31)

        # while index < n and s[index] == ' ':
        #     index += 1

        # # if all are spaces, return 0
        # if index == n:
        #     return result

        # if s[index] == '-':
        #     sign = -1
        #     index += 1
        # elif s[index] == '+':
        #     index += 1

        # while index < n and s[index].isdigit():
        #     digit = int(s[index])
        #     index += 1

        #     result = 10 * result + digit
        #     if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX%10):
        #         return INT_MAX if sign == 1 else INT_MIN

        # return sign * result


if __name__ == "__main__":
    s = '42'
    assert 42 == Solution().myAtoi(s)

    s = "   -42"
    assert -42 == Solution().myAtoi(s)

    s = "4193 with words"
    assert 4193 == Solution().myAtoi(s)

    s = "-91283472332"
    assert -2147483648 == Solution().myAtoi(s)
