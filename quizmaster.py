import pgzrun
TITLE = "Quiz Master"

WIDTH = 970
HEIGHT= 750

marquee_box =Rect(0,0,880,80)

question_box = Rect (0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)

skip_box = Rect(0,0,15,330)


answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count = 0 
question_index = 0

score=0
time_left = 10
marquee_message = ""
is_game_over = False


marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)



def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")

    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"navy blue")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"dark green")
    
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"dark orange")

    marquee_message="Welcome to the Quiz Master....."+ f" Q: {question_index} of {question_count}"

    screen.draw.text(marquee_message, marquee_box, color="white")
    screen.draw.text("Skip", skip_box,color="black", angle=90)
    screen.draw,text(str(time_left),timer_box,color="white", shadow(0,5,0.5),scolor=dim grey)







pgzrun.go()