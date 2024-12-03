def main():
    def foo():
        i = 0
        maxx = 3

        while i <= maxx:
            user_input = input("Press 'c' to eat cookie")
            if user_input == "c":
                i += 1
                if i < maxx:
                    
                    print(f" you have pressed {i} cookie(s)")
                elif i == maxx:
                    print(f" You have eaten all {maxx} cookies") 
                    break
    foo()
if __name__ == "__main__":
    main()

