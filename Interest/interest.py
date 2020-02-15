import sys


class Interest:
    principal = 0
    rate_of_return = 0
    recurring = ""
    freq_letter = ""
    duration = 0
    principal_returns = 0
    final_returns = 0
    frequencies = {
        "w": 52,
        "m": 12,
        "y": 1,
        "": 1,
    }

    freq_words = {
        "w": "week",
        "m": "month",
        "y": "year",
        "": "year",
    }

    def calculate_annual_contributions(self):
        freq_contribution = float(input(
            f"How much are you going to contribute per {self.freq_words[self.freq_letter]} ?: "))
        self.recurring = self.frequencies[self.freq_letter] * freq_contribution

    def calculate_principal_returns(self):
        self.principal_returns = round(self.principal * (self.rate_of_return ** self.duration), 2)

    def fix_rate_of_return(self):
        self.rate_of_return = self.rate_of_return + 1

    def calculate_final_returns(self):
        self.final_returns = 0
        for i in range(1, self.duration + 1):
            exponent = self.duration - i + 1
            self.final_returns += self.recurring * self.rate_of_return ** exponent
        self.final_returns += self.principal_returns
        print("Your returns: $" + str(round(self.final_returns, 2)))


if __name__ == "__main__":
    interest = Interest()
    print(sys.argv)
    # just the call
    if len(sys.argv) == 1:
        interest.principal = float(input("What is your starting amount: "))
        recurring_flip = str(input("Are you going to make recurring contributions? (y/n): "))
        if recurring_flip == "y":
            interest.freq_letter = str(input(
                "How frequently are you going to contribute? ((w)eekly, (m)onthly, (y)early): "))
            interest.calculate_annual_contributions()
        interest.rate_of_return = float(
            input("What is your expected annual rate of return (10% = .1)?: "))
        interest.fix_rate_of_return()

        interest.duration = int(input("What is your duration in years?: "))
        interest.calculate_principal_returns()

        if recurring_flip == "y":
            interest.calculate_final_returns()
        else:
            print("Your returns: $" + str(interest.principal_returns))
