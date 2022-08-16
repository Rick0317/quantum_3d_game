from math import sqrt, atan

def h_transform(quantum_state):
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = -(quantum_state.z - 10)

    pointer_x = relative_x * 2/5
    pointer_y = relative_y * 2/5
    pointer_z = relative_z * 2/5
    
    if (sqrt(1-pointer_z))*((pointer_y+pointer_z+1)**2+pointer_x**2) != 0:
        common = sqrt(2)*(1+pointer_z)/((sqrt(1-pointer_z))*((pointer_y+pointer_z+1)**2+pointer_x**2))
        pointer_x2 = common*(-sqrt(2))*pointer_x*(pointer_y+1)
        pointer_y2 = pointer_z
        pointer_z2 = common*sqrt(2)*(pointer_y**2 + pointer_y)
    elif pointer_z==1:
        pointer_x2=0
        pointer_y2=1
        pointer_z2=0
    elif ((pointer_y+pointer_z+1)**2+pointer_x**2) == 0 and pointer_z==-1:
        pointer_x2=0
        pointer_y2=-1
        pointer_z2=0
    elif ((pointer_y+pointer_z+1)**2+pointer_x**2) == 0 and pointer_y==-1:
        pointer_x2=0
        pointer_y2=0
        pointer_z2=-1
        
    quantum_state.x = pointer_x2*5/2  
    quantum_state.y = pointer_y2*5/2 + 5
    quantum_state.z = -pointer_z2*5/2 + 10

    if pointer_y - pointer_y2 != 0:
        quantum_state.rotation_x = atan((pointer_z - pointer_z2)/ (pointer_y - pointer_y2))
    if pointer_z - pointer_z2 != 0:
        quantum_state.rotation_y = atan((pointer_x - pointer_x2)/ (pointer_z - pointer_z2))
    if pointer_x - pointer_x2 != 0:
        quantum_state.rotation_z = atan((pointer_y - pointer_y2)/ (pointer_x - pointer_x2))

def x_transform(quantum_state):
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = quantum_state.z - 10

    pointer_x2 = relative_x
    pointer_y2 = -relative_y
    pointer_z2 = -relative_z

    quantum_state.x = pointer_x2
    quantum_state.y = pointer_y2 + 5
    quantum_state.z = pointer_z2 + 10

def z_transform(quantum_state):
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = quantum_state.z - 10

    pointer_x2 = (-1)*relative_x
    pointer_y2 = relative_y
    pointer_z2 = (-1)*relative_z

    quantum_state.x = pointer_x2
    quantum_state.y = pointer_y2 + 5
    quantum_state.z = pointer_z2 + 10

def s_transform(quantum_state):
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = -(quantum_state.z - 10)

    pointer_x = relative_x * 2/5
    pointer_y = relative_y * 2/5
    pointer_z = relative_z * 2/5

    pointer_x2=pointer_z
    pointer_y2=pointer_y
    pointer_z2=(-1)*pointer_x

    quantum_state.x = pointer_x2*5/2  
    quantum_state.y = pointer_y2*5/2 + 5
    quantum_state.z = -pointer_z2*5/2 + 10

def t_transform(quantum_state):
    relative_x = quantum_state.x - 0
    relative_y = quantum_state.y - 5
    relative_z = -(quantum_state.z - 10)

    pointer_x = relative_x * 2/5
    pointer_y = relative_y * 2/5
    pointer_z = relative_z * 2/5

    pointer_x2=(pointer_z+pointer_x) /sqrt(2)
    pointer_y2=pointer_y
    pointer_z2=(pointer_z-pointer_x) / sqrt(2)

    quantum_state.x = pointer_x2*5/2  
    quantum_state.y = pointer_y2*5/2 + 5
    quantum_state.z = -pointer_z2*5/2 + 10
    