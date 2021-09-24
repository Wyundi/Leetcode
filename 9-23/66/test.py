def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
        else:
            break

    return digits

if __name__ == '__main__':
    plusOne([1,2,3,5])