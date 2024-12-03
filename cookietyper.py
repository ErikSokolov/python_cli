def main():
    def foo():
        i = 0
        maxx = 10


        while i != maxx:
            user_input = input("c?")
            while i != maxx-1:
                if user_input == "c":
                    i += 1
                    print(f" you have pressed {i} cookie(s)")
            if i == maxx:
                if user_input == "c":
                    print(f"You have pressed all {maxx} cookies")
            
    foo()
if __name__ == "__main__":
    main()

