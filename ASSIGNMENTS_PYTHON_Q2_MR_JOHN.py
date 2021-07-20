class wall:
    def inputLength(self):
        print("Width of Wall : ")
        feet = float(input("Enter the length of wall in foot : "))
        inch = float(input("Enter the length of wall in inch : "))
        widthMeter = feet * 0.3048 + inch * 0.0254
        print("Height of wall : ")
        feet = float(input("Enter the length of wall in foot : "))
        inch = float(input("Enter the length of wall in inch : "))
        heightMeter = feet * 0.3048 + inch * 0.0254
        return round(heightMeter, 2), round(widthMeter, 2)

    def Area(self, height, width):
        area = height * width
        return round(area, 2)

    def Cost(self, area):
        cost = 120 * area
        return round(cost, 2)


if __name__ == "__main__":
    print("================ Enter the detail of wall 1 ===============")
    wall1 = wall()
    height1, width1 = wall1.inputLength()
    area1 = wall1.Area(height1, width1)
    cost1 = wall1.Cost(area1)
    print("============= Enter the detail of wall 2 ==================")
    wall2 = wall()
    height2, width2 = wall2.inputLength()
    area2 = wall2.Area(height2, width2)
    cost2 = wall2.Cost(area2)
    print("Bill  : -->")
    print("Height of both the wall respectively ", height1, "meter ", height2, "meter")
    print("Width of both the wall respectively ", width1, "meter ", width2, "meter")
    print("Area of both the wall respectively ", area1, "Sq. meter ", area2, "Sq. meter")
    print("Cost of both the wall respectively ", cost1, "Rs ", cost2, "Rs")
    print("Total cost :", round((cost1 + cost2), 2))
