# write your code here
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30 
    elif court_type == "outdoor":
        return 20 
    else:
        return ("try again")
def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140 
    elif racket_brand =="Siux":
        return 200
    else:
        return("try again")
  
    
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2 :
        return  3.5
    elif ball_boxes == 3 :
        return 5
    else:
        return("try again")

def padel_game_cost():
    court_type = input("Enter Court Type :")
    racket_brand = input("Enter racket brand : ")
    ball_boxes = int(input("Enter the number of ball boxes :  "))

    game = padel_court_cost(court_type)+rackets_cost(racket_brand)+padel_balls_cost(ball_boxes)
    return game 

print(padel_game_cost())


    