def main():
    def foo():
        i = 0
        maxx = 10
        cookie = []


        while i != maxx -1:
            foo = input("foo")
            cookie.append(foo)
            if cookie == "c":
                i += 1
                print(f" you have pressed {i} cookie(s)")
        else:
            print(f"You have pressed all {maxx} cookies")
            
    foo()
if __name__ == "__main__":
    main()

