from sys import argv, exit
import pprint

def read_array(filename):
    try:
        with open(filename) as f:
            return [int(n) for n in f.read().split()]
    except:
        exit("Couldn’t read numbers from file \""+filename+"\"")

def count_inversions(in_list):
    ##print("Current List: {}".format(in_list))
    invCount = 0
    if len(in_list) > 1:
        midIndex = len(in_list)//2
        l_list = in_list[:midIndex]
        r_list = in_list[midIndex:]
        ##print("Left List: {}".format(l_list))
        ##print("Right List: {}".format(r_list))
        
        
        invCount += count_inversions(l_list)
        invCount += count_inversions(r_list)
        invCount += merge_i(l_list, r_list, in_list)
        
    return invCount

def merge_i(l_list, r_list, in_list):
    invCount = 0
    i = j = k = 0
    while i < len(l_list) and j < len(r_list):
        if l_list[i] <= r_list[j]:
            in_list[k] = l_list[i]
            i += 1
        else:
            in_list[k] = r_list[j]
            invCount += len(l_list) - i
            j += 1
        k += 1
    while i < len(l_list):
        in_list[k] = l_list[i]
        i += 1
        k += 1
    while j < len(r_list):
        in_list[k] = r_list[j]
        j += 1
        k += 1
    ##print("Left and Right Merged: {}".format(in_list))
    ##print("Inversion Count: {}".format(invCount))
    return invCount

if __name__ == '__main__':
    if len(argv) != 2:
        exit("usage: python3 "+argv[0]+" datafile")
    in_list = read_array(argv[1])
    print(count_inversions(in_list))
