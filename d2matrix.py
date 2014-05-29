from scipy.sparse import dia_matrix, eye, kron
from scipy.sparse.linalg import factorized
from numpy import ones
def d2matrix(nelem):
    elements = ones((3,nelem))
    elements[1,:] *= -2
    return dia_matrix((elements, [-1,0,1]), shape=(nelem,nelem)).tocsc()
