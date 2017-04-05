import random

while True:
  command = int(input('你是否要與電腦進行猜拳對戰？1.對戰 2.退出'))
  if command == 1:
    choice = int(input('你要出？1.剪刀 2.石頭 3.布'))
    cChoice = random.randint(1, 3)
    
    if choice == 1:
      print('你出的是剪刀！')
      if cChoice == 1:
        print('電腦出的是剪刀，平手')
      elif cChoice == 2:
        print('電腦出的是石頭，你輸了')
      elif cChoice == 3:
        print('電腦出的是布，你贏了')
        
    elif choice == 2:
      if cChoice == 1:
        print('電腦出的是剪刀，你贏了')
      elif cChoice == 2:
        print('電腦出的是石頭，平手')
      elif cChoice == 3:
        print('電腦出的是布，你輸了')
        
    elif choice == 3:
      if cChoice == 1:
        print('電腦出的是剪刀，你輸了')
      elif cChoice == 2:
        print('電腦出的是石頭，你贏了')
      elif cChoice == 3:
        print('電腦出的是布，平手')
    
    else:
      print('別亂出拳！')
        
  elif command == 2:
    print('你已退出對戰')
    break;
    
  else:
    print('我不認識你輸入的命令，請重新輸入！')
  