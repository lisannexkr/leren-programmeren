dag = input("Welke dag? ").lower()
print_dag = ''
teller = 1

while print_dag != dag:
    if teller == 1:
        print_dag = 'maandag'
    elif teller == 2:
        print_dag = 'dinsdag'
    elif teller == 3:
        print_dag = 'woensdag'
    elif teller == 4:
        print_dag = 'donderdag'
    elif teller == 5:
        print_dag = 'vrijdag'
    elif teller == 6:
        print_dag = 'zaterdag'
    elif teller == 7:
        print_dag = 'zondag'

    teller = teller + 1
    print(print_dag)