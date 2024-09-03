def main(gate: str):
  match gate:
    case "Not":
      for i in range(0, 16):
        print(f"{gate}(in=in[{i}], out=out[{i}]);")
    case "And" | "Or":
      for i in range(0, 16):
        print(f"{gate}(a=a[{i}], b=b[{i}], out=out[{i}]);")
    case "Mux":
      for i in range(0, 16):
        print(f"{gate}(a=a[{i}], b=b[{i}], sel=sel, out=out[{i}]);")
    case "MultiWay":
      type: str = input()
      print(f"{type}(a=in[0], b=in[1], out=tmp1);")
      for i in range(1, 6):
        print(f"{type}(a=tmp{i}, b=in[{i + 1}], out=tmp{i+1});") 
      print(f"{type}(a=tmp6, b=in[7], out=out);")
    case _:
      raise Exception("Can't help you with that.")

if __name__ == "__main__":
  gate = input().strip()
  main(gate)
