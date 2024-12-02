def main():
    def foo():
        i = 0
        maxx = 10


        while i != maxx-1:
            user_input = input("c?")
            if user_input == "c":
                i += 1
                print(f" you have pressed {i} cookie(s)")
        else:
            print(f"You have pressed all {maxx} cookies")
            
    foo()
if __name__ == "__main__":
    main()

