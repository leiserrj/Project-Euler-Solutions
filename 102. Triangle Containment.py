def contains(points):
    if areaTri(points[:4]+[0,0]) + areaTri(points[2:]+[0,0]) + areaTri(points[:2]+points[4:]+[0,0]) == areaTri(points):
        return True
    return False

def areaTri(points):
    return abs(.5*((int(points[0])-int(points[4])) * (int(points[3])-int(points[1])) - (int(points[0])-int(points[2])) * (int(points[5])-int(points[1]))))


file = open("triangles.txt","r")
triangles = []
for line in file:
    triangles.append(line.strip().split(','))
origin = 0
for points in triangles:
    if contains(points):
        origin += 1
print(origin)