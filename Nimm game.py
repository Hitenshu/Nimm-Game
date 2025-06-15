def main():
   stones = 20
   player = 1
   while stones > 0:
    print("There are",stones,"stones left.")
    take = int(input("Player "+str(player)+" would you like to remove 1 or 2 stones? "))
    while take < 1 or take > 2:
        take = int(input("Please enter 1 or 2: "))
    print("")
    stones -= take
    if player==1:
        player=2
    else:
        player = 1

   print("Player",player,"wins!")

if __name__ == '__main__':
    main()