def question():
  print("Enter two integers")
  num1,num2 = input().split()
  print("1:ADD")
  print("2:MUL")
  print("3:SUB")
  print("4:DIV")
  choice = int(input())
  answer(num1,num2,choice)
  
def replay():
    print("Wanna ask another question(y/n)")
    ans = input()
    if ans.lower() == "y":
      question()
    elif ans.lower() == "n":
      exit()
    else:
      print("Enter a valid answer") 
      replay()

def answer(num1,num2,choice):
    if choice > 4 or choice < 1:
      print("Enter a choice lesser than 4 or greater than 1")
      question()
    if choice == 1:
      try:
        if "." in num1: 
          num1 = float(num1)
        else:
          num1 = int(num1)
        if "." in num2:
          num2 = float(num2)
        else:
          num2 = int(num2)
      except:
        print("Character cannot be changed to int or float")
        replay()
      else:
        print(num1+num2)
        replay()
    elif choice == 2:
      try:
        if "." in num1: 
          num1 = float(num1)
        else:
          num1 = int(num1)
        if "." in num2:
          num2 = float(num2)
        else:
          num2 = int(num2)
      except:
        print("Character cannot be changed to int or float")
        replay()
      else:
          print(num1*num2)
          replay()
    elif choice == 3:
      try:
        if "." in num1: 
          num1 = float(num1)
        else:
          num1 = int(num1)
        if "." in num2:
          num2 = float(num2)
        else:
          num2 = int(num2)
      except:
        print("Character cannot be changed to int or float")
        replay()
      else:
        if num1>num2:
          print(num1-num2)
          replay()
        elif num2>num1:
          print(num2-num1)
          replay()
        else:
          print(num1-num2)
          replay()
    elif choice == 4:
      if type(num1)==int and type(num2)==int:
         if num1==0 and num2==0:
            print("Cannot divide 0")
            num1,num2 = input("Enter the two integers again ").split()
            return answer(str(num1),str(num2),choice)
         elif num1==0:
            print("Cannot divide 0")
            num1 = input("Enter new num1 ")
            return answer(str(num1),str(num2),choice)
         elif num2==0:
            print("Cannot divide 0")
            num2 = input("Enter new num2 ")
            return answer(str(num1),str(num2),choice)
         if num1<num2:
            print("Enter valid integers")
            question()
         else:
            print(num1/num2)
            replay()
      else:
          try:
            if "." in num1: 
              num1 = float(num1)
            else:
              num1 = int(num1)
            if "." in num2:
              num2 = float(num2)
            else:
              num2 = int(num2)
          except:
            print("Character cannot be changed to int or float")
            replay()
          else:
            if num1==0 and num2==0:
                print("Cannot divide 0")
                num1,num2 = input("Enter the two integers again ").split()
                return answer(str(num1),str(num2),choice)
            elif num1==0:
                print("Cannot divide 0")
                num1 = input("Enter new num1 ")
                return answer(str(num1),str(num2),choice)
            elif num2==0:
                print("Cannot divide 0")
                num2 = input("Enter new num2 ")
                return answer(str(num1),str(num2),choice)
            if num1<num2:
                print("Enter valid integers")
                question()
            else:
                print(num1/num2)
                replay()

question()

