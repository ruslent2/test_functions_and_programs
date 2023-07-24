def del_substring(main_str, del_str):
    cur = 0
    dbug = False

    if del_str in main_str:
        for m in main_str:

            if dbug: print("m:", m, " cur:", cur, sep='')
            if m == del_str[0]:

                for n in list(range(0, len(del_str))):

                    if del_str[n] != main_str[cur + n]:
                        if dbug: print(del_str[n], "!=", main_str[cur + n], "didn't match n:", n)
                        break
                else:
                    if dbug: print("del:", main_str[cur:cur + len(del_str)])
                    main_str = main_str[:cur] + main_str[cur + len(del_str):]
                    cur -= len(del_str)
            cur += 1
    return main_str


if __name__ == "__main__":
    test = "Remove Usin Characters From a String Using the replace() Method"
    remu = "Using"

    print(test)
    print(del_substring(test, remu))

    # listener = list(range(0, 15)) # input("del:")
    # print(repr(listener))

    # text = "0123456789"
    # text = text[:5] + text[8:]
    # # text[19:23] = ''
    # print(repr(text))
