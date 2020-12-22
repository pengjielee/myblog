## fibonacci

```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

F(n) = F(n-1) + F(n-2)
```

## While loop

```
function fibonacci(num){
  var a = 1, b = 0, temp;
  while (num >= 0){
    temp = a;
    a = a + b;
    b = temp;
    num--;
  }
  return b;
}

Time complexity: O(N)
Space complexity: Constant
```

## Recursion

```
function fibonacci(num) {
  if (num <= 1) return 1;
  return fibonacci(num - 1) + fibonacci(num - 2);
}
Time complexity: O(2^N)
Space complexity: O(n)
```

## Memoization

```
function fibonacci(num, memo) {
  memo = memo || {};
  if (memo[num]) return memo[num];
  if (num <= 1) return 1;
  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
}

Time complexity: O(2N)
Space complexity: O(n)
```