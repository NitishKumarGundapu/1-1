from math import *

#function to print the polynominal when the coefficients are real numbers
def print_poly(poly):
    co = ""
    n = len(poly)
    for a in range(n):
        if poly[a] != 0:
            if poly[a] < 0:
                co += "- ("+str(abs(poly[a]))+") x*"+str(a)
            elif poly[a] > 0:
                if a == 0:
                    co += "("+str(poly[a])+") x*"+str(a)
                else:
                    co += "+ ("+str(poly[a])+") x*"+str(a)
        co += " "
    print(co)

#function to print the polynominal when the coefficients are complex numbers
def print_poly_fft(poly):
    n = len(poly)
    poly = [real_com(a) for a in poly]
    poly == poly[::-1]
    co = ""
    for a in range(n):
        try:
            if int(poly[a][1]) == 0:
                if poly[a][0] < 0:
                    co += "- ("+str(abs(poly[a][0]))+") x*"+str(a)
                elif poly[a][0] > 0:
                    if a == 0:
                        co += "("+str(poly[a][0])+") x*"+str(a)
                    else:
                        co += "+ ("+str(poly[a][0])+") x*"+str(a)
            elif int(poly[a][1]) < 0:
                if poly[a][0] < 0:
                    co += "- ("+str(abs(poly[a][0]))+" - "+str(abs(poly[a][1]))+") x*"+str(a)
                elif poly[a][0] > 0:
                    if a == 0:
                        co += "("+str(poly[a][0])+" - "+str(abs(poly[a][1]))+") x*"+str(a)
                    else:
                        co += "+ ("+str(poly[a][0])+" - "+str(abs(poly[a][1]))+") x*"+str(a)
            elif int(poly[a][1] > 0):
                if poly[a][0] < 0:
                    co += "- ("+str(abs(poly[a][0]))+" + "+str(abs(poly[a][1]))+") x*"+str(a)
                elif poly[a][0] > 0:
                    if a == 0:
                        co += "("+str(poly[a][0])+" + "+str(abs(poly[a][1]))+") x*"+str(a)
                    else:
                        co += "+ ("+str(poly[a][0])+" + "+str(abs(poly[a][1]))+") x*"+str(a)
            co += " "
        except:
            continue
    print(co)

#naive polynomial multiplication wich takes O(n2) time complexity
def naive_polynomial_multiplication(poly_1,deg_1,poly_2,deg_2):
    res = [0]*(deg_1+deg_2+1)
    for a in range(deg_1+1):
        for b in range(deg_2+1):
            res[a+b] += poly_1[a]*poly_2[b]
    return res

#anonymous function which takes a,b two complex numbers as argumants and gives the addition
#of the given two complex numbers  
add_complex_num = lambda a,b : [a[0]+b[0],a[1]+b[1]]

#anonymous function which takes a,b two complex numbers as argumants and gives the subtraction
#of the given two complex numbers  
sub_complex_num = lambda a,b : [a[0]-b[0],a[1]-b[1]]

#anonymous function which takes a,b two complex numbers as argumants and gives the multiplication
#of the given two complex numbers  
multiply_complex_num = lambda a,b : [a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]]

#function which converts number into complex
#here complex means a list of size 2 having 1 real and 1 imaginary parts as components
def real_com(a):
    if type(a) == list and len(a) == 2:
        return a
    elif type(a) == int:
        return [a,0]

#anonymous function which takes two arguments and returns the nearest power of 2 
find_N = lambda a,b : ceil((log(a+b+1,2)))

#anonymous function which takes n and gives n roots of unity
Nthroots = lambda n : [(round(cos((2*pi*i)/n),3),round(sin((2*pi*i)/n),3)) for i in range(1,n+1)]

#function which takes the polynomial coefficients and returns the evaluations of the polynomial 
def Eval(poly):
    n = len(poly)
    if n == 1:
        return poly
    wn = [round(cos((2*pi)/n),3),round(sin((2*pi)/n),3)]
    w = real_com(1)
    even_poly , odd_poly = poly[::2],poly[1::2]
    res_even , res_odd = Eval(even_poly), Eval(odd_poly)
    res = [0]*n
    for a in range(n//2):
        res[a] = add_complex_num(real_com(res_even[a]) , multiply_complex_num(w,real_com(res_odd[a])))
        res[a+(n//2)] = sub_complex_num(real_com(res_even[a]) , multiply_complex_num(w,real_com(res_odd[a])))
        w = multiply_complex_num(w,wn)
    return res

#function which takes 2 polynomial evalutations and returns the product evaluations 
def product_polynomial_evaluations(eval1,eval2):
    return [multiply_complex_num(a,b) for a,b in zip(eval1,eval2)]

#function which takes the product polynomaial evaluations and returns the coefficients of the 
#product polynomial.
def Inverse_Eval(poly):
    n = len(poly)
    if n == 1:
        return poly
    wn = [round(cos((-1*2*pi)/n),3),round(sin((-1*2*pi)/n),3)]
    w = real_com(1)
    even_poly , odd_poly = poly[::2],poly[1::2]
    res_even , res_odd = Inverse_Eval(even_poly), Inverse_Eval(odd_poly)
    res = [0]*n
    for a in range(n//2):
        res[a] = add_complex_num(real_com(res_even[a]) , multiply_complex_num(w,real_com(res_odd[a])))
        res[a+(n//2)] = sub_complex_num(real_com(res_even[a]) , multiply_complex_num(w,real_com(res_odd[a])))
        w = multiply_complex_num(w,wn)
    return res

#main function where the code starts
def main():
    poly_1 = [0]*16
    poly_2 = [0]*16
    naive_poly = [0]*32
    fft_poly = [0]*32

    #taking the inputs
    deg_1 = int(input("enter the degree of 1st polynomial : "))
    t1 = list(map(int,input("enter the "+str(deg_1+1)+" coefficients of 1st polynomial in the increasing order of degree of monomials: ").split()))
    for _ in range(len(t1)): poly_1[_] = t1[_]

    deg_2 = int(input("enter the degree of 2nd polynomial : "))
    t2 = list(map(int,input("enter the "+str(deg_2+1)+" coefficients of 2nd polynomial in the increasing order of degree of monomials: ").split()))
    for _ in range(len(t2)): poly_2[_] = t2[_]

    #printing the polynomials
    print("\nthe first polynomial is : \n")
    print_poly(poly_1)
    print("\nthe second polynomial is : \n")
    print_poly(poly_2)

    #naive_polynomail_multiplication
    t3 = naive_polynomial_multiplication(poly_1,deg_1,poly_2,deg_2)
    for _ in range(len(t3)): naive_poly[_] = t3[_]

    #getting polynomial evaluations using Eval(FFT)
    n = find_N(deg_2,deg_1)
    eval1 = Eval(poly_1[:2**n])
    eval2 = Eval(poly_2[:2**n])

    #getiing product polynomial evalutations
    coeffs = product_polynomial_evaluations(eval1, eval2)

    #getting ans adjusting product polynomial using Inverse FFT
    n1 = len(coeffs)
    t4 = [[round(a[0]/n1),round(a[1]/n1)] for a in Inverse_Eval(coeffs)]
    for _ in range(len(t4)): fft_poly[_] = t4[_]

    #Printing the polynomails
    print("\n the product of two polynomials obtained via naive polynomial multiplication is : \n")
    print_poly(naive_poly)
    print("\n the product of two polynomials obtained via fft is : \n")
    print_poly_fft(fft_poly)

main()