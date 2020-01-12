tmp = var1
var1 = var2
var2 = tmp
print(f'var1 vaut {var1}, var2 vaut {var2}')

# without temporary variable

var1 += var2
var2 = var1 - var2
var1 -= var2
print(f'var1 vaut {var1}, var2 vaut {var2}')