def d():
    animal = "element"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside the nested function: ", + animal)

    print("before calling the function: ",animal)
    e()
    



