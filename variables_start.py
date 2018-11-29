#
# Example file for variables
#

# Declare a variable and initialize it
f=0


# # re-declaring the variable works


# # ERROR: variables of different types cannot be combined


# Global vs. local variables in functions
def somefunction():
    #global f
    f="global_f"
    print(f)
somefunction()
print(f)

del f
print(f)
