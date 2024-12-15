import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
s_list = data["state"].tolist()
n_list = []
score = 0

title = "Guess the state"
while len(n_list) < 50:
    answer_state = screen.textinput(title=f"{title}", prompt="Whats another states name")
    ans = answer_state.title()
    if ans == "Exit":
        break
    if ans in s_list:
        score += 1
        n_list.append(ans)
        title = f"Score: {score}/50"
        x = int(data[data.state == ans]["x"])
        y = int(data[data.state == ans]["y"])
        tim = turtle.Turtle()
        tim.penup()
        tim.goto(x, y)
        tim.write(ans, False, align="center", font=("Arial",8,"normal"))
o_list = []
for state in s_list:
    if state not in n_list:
        o_list.append(state)

s_dic = {
    "states": o_list
}

nd = pandas.DataFrame(s_dic)
nd.to_csv("states_to_learn.csv")

