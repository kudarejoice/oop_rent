class rentalProperty():
    def __init__(self, investment = '', gain = ''):
        self.investment = investment
        self.gain = gain
        
    def calculator(self):
        while True:
            print("Let's calculate your ROI for the rental property.")
            self.gain = input("How much did you get back on the property? 'Quit?'" "\n")
            self.investment = input("How much did you invest in the property? 'Quit?'" "\n")
            
            calculation = (( int(float(self.gain)) - int(float(self.investment))) / int(float(self.investment)))
            percentage = "{:.2%}".format(calculation)
            print(percentage)
            break
roi_calc = rentalProperty()

def response():
    while True:
        print("Welcome to your Return on investment Calculator.")
        response = input("What would you like to do?" "\nCalculate ROI" "\nQuit" "\n")
        if response.lower() == 'quit':
            print("Thank you, have a nice day!")
            break
        elif response.lower() == 'calculate roi':
            roi_calc.calculator()
            print("That's your ROI. Have a nice day!")
            break
response()

