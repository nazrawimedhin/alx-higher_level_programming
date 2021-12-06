def safe_print_list(my_list=[], x=0):
    counted = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except:
            break
        else:
            counted += 1
        print('')
    return(counted)

