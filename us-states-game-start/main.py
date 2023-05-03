import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
correct_answers_count = 0
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state: {correct_answers_count}/50", prompt="What are the states "
                                                                                                 "in U.S.?").title()
    states_list = pandas.read_csv('50_states.csv')
    all_states = states_list.state.to_list()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # Commented out portion can be done using one line
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        correct_answer = states_list[states_list.state == answer_state]
        new_x = correct_answer.x
        new_y = correct_answer.y
        correct_answers_count += 1
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(int(new_x), int(new_y))
        state_turtle.write(f"{answer_state}")

# if answer_state.lower() in states_list.state.lower():
# new_x = states_list[states_list.state.lower == answer_state.lower()].x
# new_y = states_list[states_list.state.lower == answer_state.lower()].y

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()