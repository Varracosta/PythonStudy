
class Robot:

    num_of_robots = 0

    def __init__(self, inp_str):
        self.model, self.name = inp_str.split("-")
        Robot.num_of_robots += 1

    def display_robot_info(self):
        print(f"Model: {self.model} \n Name: {self.name}")


optimus = Robot("autobot-Optimus")
walle = Robot("janitor-Walle")

optimus.display_robot_info()
walle.display_robot_info()
