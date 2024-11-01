import math

def calculate_point_Q():
    # Step 3: Verify that point P lies on the circumference of the circle
    x_p, y_p = 3, 4  # Coordinates of point P
    radius_squared = 25  # Radius squared of the circle
    if x_p**2 + y_p**2 == radius_squared:
        print("Point P lies on the circumference of the circle.")
    else:
        print("Point P does not lie on the circumference of the circle.")

    # Step 4: Find the direction vector from point P to the origin (0,0)
    direction_vector_x = 0 - x_p
    direction_vector_y = 0 - y_p

    # Step 5: Find the coordinates of point Q
    distance_pq = math.sqrt(10)

    # Normalize the direction vector
    magnitude = math.sqrt(direction_vector_x**2 + direction_vector_y**2)
    unit_vector_x = direction_vector_x / magnitude
    unit_vector_y = direction_vector_y / magnitude

    # Calculate the coordinates of point Q
    x_q = x_p + unit_vector_x * distance_pq
    y_q = y_p + unit_vector_y * distance_pq

    return (x_q, y_q)

# Execute the function
point_Q = calculate_point_Q()
print("Coordinates of point Q:", point_Q)
