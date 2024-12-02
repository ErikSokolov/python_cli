def main():
    def function():
        lines = int(input("foo"))
        list = []
        x = 0
        f = -1
        b = 0

        for i in range(lines):
            list.append(i+1)
        print(list)
        for i in list:
            i += 1
            print("#"*(list[x]+b) + "   " + "@"*list[f])
            f -= 1
            x += 1  
            b += 3
            
    function()
    


if __name__ == "__main__":
    main()
