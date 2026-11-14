def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    result = ""
    l =["a","e","i","o","u","A","E","I","O","U"]
    for i in word:
        if(i not in l):
            result += i

    return result
if __name__ == "__main__":
    main()
