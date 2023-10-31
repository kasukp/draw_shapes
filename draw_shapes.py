from itertools import zip_longest
import tkinter

def main():
    root = tkinter.Tk()
    w = tkinter.Canvas(root, bg='#fff', height=400, width=500)
    w.pack()
    w.update()
    canvas_h = w.winfo_height()
    canvas_w = w.winfo_width()

    class Rectangle():
        def __init__(self, *args) -> None:
            ''' 
            Plots rectangle in center of screen from parameters,
            In order: Height, Width, Color, Vertical offset, Horizontal offset
            '''
            default = [280, 400, "#009C3B", 0, 0]
            attr = ['height', 'width', 'color', 'v_offset', 'h_offset']
            for i, j, k in zip_longest(attr, args, default):
                setattr(self, i, j or k)


        def draw(self):
            w.create_rectangle((canvas_w - self.width)/2 + self.h_offset,
                                canvas_h/2 - self.height/2 + self.v_offset,
                                canvas_w/2 + self.width/2 + self.h_offset,
                                canvas_h/2 + self.height/2 + self.v_offset,
                                outline="", fill = self.color)
            return self

    class Circle():
        def __init__(self, *args) -> None:
            ''' 
            Plots circle in center of screen from parameters,
            In order: Radius, Color, Vertical offset, Horizontal offset
            '''
            default = [70, "#002776", 0, 0]
            attr = ["radius", "color", "v_offset", "h_offset"]
            for i, j, k in zip_longest(attr, args, default):
                setattr(self, i, j or k)

        def draw(self):
            w.create_oval(canvas_w/2 - self.radius + self.h_offset,
                        canvas_h/2 - self.radius + self.v_offset,
                        canvas_w/2 + self.radius + self.h_offset,
                        canvas_h/2 + self.radius + self.v_offset,
                        outline = "",
                        fill = self.color)
            return self

    class Diamond():
        def __init__(self, *args) -> None:
            ''' 
            Plots diamond in center of screen from parameters,
            In order: Height, Width, Color, Vertical offset, Horizontal offset
            '''
            default = [106, 166, "#FFDF00", 0, 0]
            attr = ['height', 'width', 'color', 'v_offset', 'h_offset']
            for i, j, k in zip_longest(attr, args, default):
                setattr(self, i, j or k)

        def draw(self):
            w.create_polygon(canvas_w/2 - self.width + self.h_offset,
                            canvas_h/2 + self.v_offset,
                            canvas_w/2 + self.h_offset,
                            canvas_h/2 - self.height + self.v_offset,
                            canvas_w/2 + self.width + self.h_offset,
                            canvas_h/2 + self.v_offset,
                            canvas_w/2 + self.h_offset,
                            canvas_h/2 + self.height + self.v_offset,
                            outline = "",
                            fill = self.color)
            return self

    a = Rectangle().draw()
    b = Diamond(a.height/2 - 34, a.width/2 - 34)
    b.draw()
    Circle().draw()
    # Circle(55,"#d4a",-25,35).draw()
    # Circle(55,"#d4a",-25,-35).draw()
    # Diamond(80,79,"#d4a",9).draw()
    
    # Rectangle(280, 400, "#009C3B").draw()
    # Diamond(a.height/2 - 34, a.width/2 - 34, "#FFDF00").draw()
    # Circle(70, "#002776").draw()

    root.mainloop()


if __name__ == "__main__":
    main()
