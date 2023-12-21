operation = int(input("Qual operação você deseja usar: 1(+), 2(-), 3(*), 4(/)"));
firstNumber = float(input("Qual o primeiro numero?"));
secondNumber = float(input("Qual o segundo numero?"));
match operation:
    case 1:
        print(float(firstNumber + secondNumber));
    case 2:
        print(float(firstNumber - secondNumber));
    case 3:
        print(float(firstNumber * secondNumber));
    case 4:
        print(float(firstNumber / secondNumber));