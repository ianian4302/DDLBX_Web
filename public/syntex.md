# Syntex

## End of line

In some languages like C++, you have to use semicolons to end lines of code. In DDLBX, you have to use exclamation marks!!

```dart
print("Hello world")!
```

And if this line is so important, you can use more exclamation marks to make it "more important".

```dart
print("Hello world")!!!
```

## Comments

You can use `//` to comment your code.

```dart
// This is a comment!
```

Remember to use exclamation marks to end your comments to make it "more important".

```dart
// This is a comment!!!
```

Thanks to the exclamation marks, you can use `//` in strings.

```dart
Str a = "Hello // world"!!
print(a)! // Hello
```

Of course, you can use comments in comments, but you have to use more exclamation marks to end your comments.

```dart
// This is a comment // This is a comment of comment!!
```

## Variable

Below is the variable declaration syntax.

### Integer

Integers are numbers without decimal points. They can be positive or negative.

```dart
Int a = 1!
```

### Float

Floats are numbers with decimal points. They can be positive or negative.

```dart
Flo a = 1.0!
```

### String

Strings are text. They can be declared with single quotes or double quotes.

```dart
Str a = 'Hello'!
```

### Boolean

Booleans can be `true` or `false` or `maybe`.

```dart
Boo a = true!
Boo b = false!
Boo c = maybe! // will be true or false by random!
```

### Regex

Regex is a variable type that can be used to match strings.

```dart
Reg a = @([a-z]+)!
```

It can also use with [Delete and undelete](#delete-and-undelete).

## Naming

Most of languages use English words to name variables. But in DDLBX, you can use any words in asscii.

```dart
Int a = 1!
Int 5 = 3!
Int b = 5! // 3!
```

## Operators

### Logical operators

| Operator | Description |
| -------- | ----------- |
| `and` | Logical and |
| `or` | Logical or |

### Arithmetic operators

| Operator | Description |
| -------- | ----------- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |
| `%=` | Modulus and assign |

### Comparison operators

| Operator | Description |
| -------- | ----------- |
| `==` | Equal |
| `!=` | Not equal |
| `~=` | Approximate equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

There is a thing you need to know about `~=`. It's used to check if two values are approximate equal. It's hard to say if two values are approximate equal, so it will always return `true`.

```dart
5 ~= 5! // true!
3 ~= 5! // true!
```

### Special operators

| Operator | Description |
| -------- | ----------- |
| `^` | Return `true` if code direction is up, else return `false` |
| `v` | Return `true` if code direction is down, else return `false` |

As you see, the down arrow is a little bit bigger than the up arrow. It's because we are still recommending you to write code from top to bottom.

Also, we use char v as operator, but you can still use it as a variable name because [Naming](#naming).

See [Reversing](#reversing) to have an idea why we need `^` and `v`.

## Conditionals

You can use `case` to declare conditionals.

```dart
Int a = 0!
case (a == 0) {
    print("a is 0")!
} case (a == 1) {
    print("a is 1")!
} else {
    print("a is not 0 or 1")!
}!
```

If the containing code is only one line, you can use `=>` instead of `{}`.

```dart
Int a = 0!
case (a == 0) => print("a is 0")
case (a == 1) => print("a is 1")
else => print("a is not 0 or 1")!
```

Use `!` to end your conditionals.

```dart
Int a = 0!
case (a == 0) => print("a is 0")!
```

## Loops

We don't need loops in DDLBX. We can use functions or reversing(see [Reversing](#reversing)) to implement loops.

## Functions

To declare a function, you can use any letters from the word `func`:

```dart
fun a(): void {
   print("Hello world")!
}!
```

You can also pass arguments to functions.

```dart
fun a(Int b): void {
   print(b)!
}!
```

You can also return values from functions.

```dart
fun a(): Int {
   ret 1!
}!
```

You can also use `=>` to declare a function.

```dart
fun add(Int a, Int b): Int => ret a + b!
```

If there are some spcific parameters with it's own return value, you can specify it.

See [Fibonacci](examples/fibonacci.ddlbx) for complete example.

```dart
fun fib(Int a): Int => fib(a - 1) + fib(a - 2)!
fun fib(0) => 0!
fun fib(1) => 1!
```

## Delete and undelete

You can use it to prevent some developers from using some words in compile time.

```dart
// In this FP project, we don't want developers to use obj
del @(fun)!

======= other code =======
fun obj(): void! // Error: fun has been deleted
```

```dart
// In this project, the naming rule is camelCase and we don't want developers to use snake_case, delete the regex

```dart
del @([a-z]+_[a-z]+)!

======= other code =======
Int a_b = 1! // Error: [a-z]+_[a-z]+ has been deleted
```

If you don't want to delete a variable, you can use `undel`.

```dart
del @(fun)!
undel @(fun)!
fun obj(): void! // OK
```

If you don't want to let anyone use `del` and, you can also delete it.

```dart
del @(undel)!
del @(del)!
```

## Reversing

You can Rev the direction of your code in scope.

```dart
Str message = "Hello"!
print(message)! // Hello world
message = "world"!
rev!
```

Implementing loops with reversing and conditionals.

```dart
Int a = 0!
// when code direction is reversed, ^ will be false
case (^) => rev! 
print(a)!
case (a++ < 10) => rev!
```
