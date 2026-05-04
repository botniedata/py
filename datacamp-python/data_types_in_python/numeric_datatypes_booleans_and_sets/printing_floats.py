# Values
float1 = 0.0001
float2 = 1e-05
float3 = 1e-07

""" Instructions:
1. Print float1, float2, and float3 notice where the jump to scientific notation occurs.
2. Print float2 and float3 using the default float format specifier, and notice what happened to float3.
3. Print float3 with the float format specifier and a precision of 7.
"""

# Print floats, 1, 2, and 3
print(float1)
print(float2)
print(float3)

# Print floats 2 and 3 using the f string formatter
print(f"{float2:f}")
print(f"{float3:f}")

# Print float3 with a 7 f string precision
print(f"{float3:.7f}")