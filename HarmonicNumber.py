
"""
   * Author - Avinash patil
   * Date -  21-01-2022
   * Time -  1.20pm
   * Title - Harmonic Series
"""
try:
    n = int(input("Enter nth number:"))

    def harmonic_sum(n):

        if n < 2:
            return 1
        else:
            return 1 / n + (harmonic_sum(n - 1))

    print(harmonic_sum(n))

except Exception as e:
    print("Enter Numeric Value", e)