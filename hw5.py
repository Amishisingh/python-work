
print(" SMART SWITCH MONITOR")
n = int(input("Enter switch status number: "))

print(" SWITCH STATUS SCAN ")

temp = n
switch = 1

while temp > 0:
    bit = temp & 1

    if bit == 1:
        print("Switch", switch, ": ON")
    else:
        print("Switch", switch, ": OFF")

    temp >>= 1
    switch += 1

# Display binary status
print("\n--- MONITOR RESULTS ---")
print("Switch status:", n)
print("Binary status:", bin(n)[2:])
print("Total switches:", len(bin(n)[2:]))
print("Switches ON:", bin(n).count('1'))
print("Switches OFF:", len(bin(n)[2:]) - bin(n).count('1'))

print("\nSMART SWITCH MONITOR COMPLETE!")
print("================================")
