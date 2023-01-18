import sys
motion = sys.stdin.readline().strip()
left = ""; right = ""; face = "(^0^)"; where_is_face = 0
if face in motion:
    where_is_face_l = motion.find("(")
    where_is_face_r = motion.find(")")
    left += motion[:where_is_face_l]
    right += motion[where_is_face_r+1:]
print("{} {}".format(left.count("@"), right.count("@")))