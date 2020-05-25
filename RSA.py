

def get_PhiN(P,Q):
    return (P-1)*(Q-1)


def extended_euclid(a, b):
    if a == 0:
        return (0, 1)
    else:
        x, y = extended_euclid(b % a, a)
        return ( y - (b//a) * x, x)

def find_inverse(a,b):
    (inv,_) = extended_euclid(a,b)
    if inv < 0:
        inv = inv + b
    return inv


def FME( base, exp, mod): 
    twos = [1,2]
    squares = [base]
    two_square = 2
    square = base
    while two_square<= exp:
        two_square *= 2
        twos += [two_square]
        square = (square**2) % mod
        squares += [square]
    result = 1
    i = len(twos) - 1
    while exp != 0:
        while twos[i] <= exp:
            exp -= twos[i]
            result = (result*squares[i]) % mod
        i -= 1
    return result




def convert_to_string( num):
    alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",\
            "k", "l","m", "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    table_27 = [1,27]
    cur = 27
    while num > cur:
        cur *= 27
        table_27 += [cur]
    i = len(table_27) - 1
    word = [0]*(i+1)
    
    while num != 0:
        count = 0
        while table_27[i] <= num :
            num -= table_27[i]
            count += 1
        word[i] = count
        i -= 1
        
    word.reverse();
    return "".join(map(lambda x: alphabet[x], word))

def word_to_int(word): #just for testing
    alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",\
            "k", "l","m", "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    c_list = list(word)
    c_list.reverse()

    place = 1 
    decimal = 0
    for i in range(len(c_list)):
        decimal += place * (alphabet.index(c_list[i]))
        place *= 27
    return decimal


def decode_message(P,Q,E,C):
    N = P*Q
    phiN = get_PhiN(P,Q)

    Einv = find_inverse(E,phiN)

    M = FME(C,Einv,N)

    return convert_to_string(M)


def encode_message(E,N,M):
    return FME(M,E,N)

def main():
    P = 435958568325940791799951965387214406385470910265220196318705482144524085345275999740244625255428455944579
    Q = 562545761726884103756277007304447481743876944007510545104946851094548396577479473472146228550799322939273
    C = 163077576587089932277514178989798339755826189700674110151160860819557757512053108465634676999401755817425637794522932574265893488854028596522889419543378155476439015236106447427921542963150735762104095795184542
    E = 7

    M = decode_message(P,Q,E,C)
    print(M)
    #we have two lives and the second one begins when we realize we only have one    confucius




if __name__ == "__main__":
    main()

