from gauss_solver import soluciona

solucao = soluciona([
  [2,2,3,1,7],
  [1,-1,3,-1,1],
  [3,2,-3,-2,4],
  [4,3,2,1,12]
])
assert solucao == [2.5227272727272734, 0.02272727272727198, 0.06818181818181789, 1.704545454545455]

solucao = soluciona([
  [3.03,-12.1,14,-119],
  [-3.03,12.1,-7,120],
  [6.11,-14.2,21,-139],
])
assert solucao == [0.0, 10.0, 0.14285714285714285]

solucao = soluciona([
  [1.19,2.11,-100,1,1.12],
  [14.2,-0.122,12.2,-1,3.44],
  [0,100,-99.9,1,2.15],
  [15.3,0.11,-13.1,-1,4.16]
])
assert solucao == [0.17682529749934564, 0.012692690867687546, -0.020654050137131074, -1.1826086954681492]

solucao = soluciona([
  [1,0.5,0.333,2],
  [0.5,0.333,0.25,-1],
  [0.333,0.25,0.2,0],
])
assert solucao == [58.84947507211686, -289.2021237702332, 263.5182787177169]

print("Tudo certo.")