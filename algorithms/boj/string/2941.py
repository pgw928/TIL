import sys
st = sys.stdin.readline().strip()

st = st.replace('c=', '1')
st = st.replace('c-', '1')
st = st.replace('dz=', '1')
st = st.replace('d-', '1')
st = st.replace('lj', '1')
st = st.replace('nj', '1')
st = st.replace('s=', '1')
st = st.replace('z=', '1')
print(len(st))
