def linearsearchproduct(productList,targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products = ["shoes","boot","loafer","shoes","sandel","shoes"]
target="shoes"
target2='apple'
result1=linearsearchproduct(products, target)
result2=linearsearchproduct(products, target2)
print(result1)
print(result2)