distance = 1.23
height = 2.34

print(f"Distance: {distance:.1f} meters, Height: {height:.1f} meters")
print("Distance: {:.1f} meters, Height: {:.1f} meters".format(distance, height))
print("Distance: {1:.1f}, Height: {0:.1f}".format(height, distance))

print("Distance: %.1f, Height: %.1f" % (distance, height))
print("one\ntwo")
print(r"one\ntwo")
print(rf"1 {distance:.1f} \n 2 {height:.1f}")