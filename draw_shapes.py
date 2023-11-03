from itertools import zip_longest
import tkinter


def main():
    root = tkinter.Tk()
    w = tkinter.Canvas(root, bg="#cdf", height=400, width=500)
    w.pack()

    input_txt = tkinter.Text(root, height=1, width=50,)
    input_txt.pack()


    w.update()
    canvas_h = w.winfo_height()
    canvas_w = w.winfo_width()

    class Rectangle():
        def __init__(self, **kwargs) -> None:
            ''' 
            Plots rectangle in center of screen from parameters.
            '''
            self.height = kwargs.get("height", 280)
            self.width = kwargs.get("width", 400)
            self.color = kwargs.get("color", "#009C3B")
            self.y_offset = kwargs.get("y_offset", 0)
            self.x_offset = kwargs.get("x_offset", 0)


        def draw(self):
            w.create_rectangle((canvas_w - self.width)/2 + self.x_offset,
                                canvas_h/2 - self.height/2 + self.y_offset,
                                canvas_w/2 + self.width/2 + self.x_offset,
                                canvas_h/2 + self.height/2 + self.y_offset,
                                outline="", fill = self.color)
            return self

    class Circle():
        def __init__(self, **kwargs) -> None:
            ''' 
            Plots circle in center of screen from parameters.
            '''
            self.radius = kwargs.get("radius", 70)
            self.color = kwargs.get("color", "#002776")
            self.y_offset = kwargs.get("y_offset", 0)
            self.x_offset = kwargs.get("x_offset", 0)

        def draw(self):
            w.create_oval(canvas_w/2 - self.radius + self.x_offset,
                        canvas_h/2 - self.radius + self.y_offset,
                        canvas_w/2 + self.radius + self.x_offset,
                        canvas_h/2 + self.radius + self.y_offset,
                        outline = "",
                        fill = self.color)
            return self

    class Diamond():
        def __init__(self, **kwargs) -> None:
            ''' 
            Plots diamond in center of screen from parameters.
            '''
            self.height = kwargs.get("height", 106)
            self.width = kwargs.get("width", 166)
            self.color = kwargs.get("color", "#FFDF00")
            self.y_offset = kwargs.get("y_offset", 0)
            self.x_offset = kwargs.get("x_offset", 0)

        def draw(self):
            w.create_polygon(canvas_w/2 - self.width + self.x_offset,
                            canvas_h/2 + self.y_offset,
                            canvas_w/2 + self.x_offset,
                            canvas_h/2 - self.height + self.y_offset,
                            canvas_w/2 + self.width + self.x_offset,
                            canvas_h/2 + self.y_offset,
                            canvas_w/2 + self.x_offset,
                            canvas_h/2 + self.height + self.y_offset,
                            outline = "",
                            fill = self.color)
            return self

    class Line():
        def __init__(self, dot):
            self.dot = dot
        def draw(self):
            mx = canvas_w/2
            my = canvas_h/2
            dot=self.dot
            w.create_line(my+dot, mx+dot, my+dot, mx+dot)

    def get_input():
        user_input = input_txt.get(1.0, "end").split()
        if user_input:
            print(*user_input)
    
    submit_button = tkinter.Button(root, text="Submit", command=get_input)
    submit_button.pack()

    # a = Rectangle().draw()
    # b = Diamond(height=a.height/2 - 34, width=a.width/2 - 34)
    # b.draw()
    # Circle().draw()

    Circle(radius = 55, color = "#d4a", y_offset = -25, x_offset = 35).draw()
    Circle(radius = 55, color = "#d4a", y_offset = -25, x_offset = -35).draw()
    Diamond(height = 80, width = 79, color = "#d4a", y_offset = 9).draw()

    # a = Rectangle(height=280, width=400, color="#009C3B").draw()
    # Diamond(height= a.height/2 - 34, width= a.width/2 - 34, color= "#FFDF00").draw()
    # Circle(radius=70, color="#002776").draw()

    root.mainloop()
    # while True:
    #     root.update()



if __name__ == "__main__":
    main()
