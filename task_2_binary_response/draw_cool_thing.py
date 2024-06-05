from l_system import LSystem, Turtle



def get_image(step=4, axiom='F-G-G', rule_F='F-G+F+G-F', rule_G='GG'):
    
    step = step

    l_system = LSystem(
        variables='FG',
        constants='+-',
        axiom=axiom,
        rules={'F': rule_F, 'G': rule_G},
    )

    s = l_system.axiom
    for n in range(step + 1):
        width = 2 if n < 3 else 1 if n < 5 else 0.5
        turtle = Turtle(
            direction=60.0,
            move_rules={
                'F': Turtle.get_go_forward('red', width),
                'G': Turtle.get_go_forward('gold', width),
                '+': Turtle.get_turn(120.0),
                '-': Turtle.get_turn(-120.0),
            },
        )

        turtle.move(s)
        if n == step:
            turtle.save(f'n = {n}', output_path=f'task_2_binary_response/static/image/cool_image.svg')
        s = l_system.step(s)


get_image()



