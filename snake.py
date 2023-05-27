from turtle import Turtle

# SET POSITION FOR TURTLE MOTION
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

MOVE = 20
# SETTING DIRECTIONS TO BE GIVEN BY USER

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    # CREATING A SNAKE USING TURTLE GRAPHICS
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def add_segment(self,position):
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        """make snake longer"""
        self.add_segment(self.segment[-1].position())

    # MOVE THAT TAKEN BY SNAKE
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE)

    # MOVING ON COMMANDS
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
