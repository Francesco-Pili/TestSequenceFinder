import re
def main():
    
    while True:
        try:
            numrows = int(input("Enter the no. of rows of blood sample tray: "))
        except ValueError:
            print("please enter a valid number")
            continue
        break
    rows = []
    for i in range(numrows):
        while True:
            try:
                newrow = input(f"Please enter row no. {i+1}: ")
                setnewrow = set(newrow)
                assert setnewrow=={'0', '1'} or setnewrow =={'0'} or setnewrow == {'1'}
            except AssertionError:
                print("please use only \'1\'s and \'0\'s")
                continue
            break
        rows.append(newrow)
    for i,r in enumerate(rows):
        consec = [len(x) for x in re.sub(" ", "",r).split('0') if x != '' and len(x) >1]
        consecstr= ", ".join([str(x) for x in consec])
        print(f"Row{i+1}: {len(consec)} {{{consecstr}}}")

main()
