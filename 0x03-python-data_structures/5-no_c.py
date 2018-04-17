#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):
        mod_string = my_string
        ret1 = my_string.find('c')
        ret2 = my_string.find('C')

        if ret2 > 0:
            mod_string = my_string[:ret2] + my_string[(ret2 + 1):]
            return mod_string
        if ret1 > 0 or ret2 > 0:
            mod_string = my_string[:ret1] + my_string[(ret1 + 1):]
            mod_string = my_string[:ret2] + my_string[(ret2 + 1):]
            return mod_string
        else:
            print("broken")
#    elif ret2 > 0:
 #       my_string = my_string[:ret1] + my_string[(ret1 + 1):]
  #      return my_string
  #  if ret2 > 0:
   #     my_string = my_string[:ret2] + my_string[(ret2 + 1):]
    #    return my_string
   # else:
    #    print("Woah")
