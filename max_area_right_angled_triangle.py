
# The area (A) of a right-angled triangle is given by:

# A = 0.5 * a * b

# where, a and b are the lengths of two sides of the triangle respectively.
def max_area_right_angle_triangle(perimeter):
    
    mx_area = mx_a = mx_b = 0
    
    for a in range(1, perimeter // 2):
        b = perimeter - a  
        area = 0.5 * a * b  
        
        if area > mx_area:
            mx_area = area
            mx_a = a
            mx_b = b
    
    return mx_area, mx_a, mx_b

if __name__ == "__main__":
    perimeter = 20
    max_area, max_a, max_b = max_area_right_angle_triangle(perimeter)
    print(f"Maximum area for a right-angled triangle with perimeter {perimeter} is {max_area:.2f} with sides {max_a} and {max_b}")
