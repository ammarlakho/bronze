
def linear_evolve(B, v):
    new_state = []
    for i in range(len(v)):
        new_state.append(0)
    for i in range(len(B)):
        for j in range(len(v)):
            new_state[i] += B[i][j]*v[j]
    return new_state
    
