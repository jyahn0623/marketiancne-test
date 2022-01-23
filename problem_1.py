
def problem_1():
    pass

def problem_2(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
    
if __name__ == '__main__':
    problem_1()
    problem_2(["12","123","1235","567","88"])
    problem_2(["123","456","789"])