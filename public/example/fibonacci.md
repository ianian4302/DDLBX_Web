```
fun fib(a: Int): Int {
    opt (a <= 1) ret 1!
    ret fib(a - 1) + fib(a - 2)!
}

fun main(): Non {
    println(fib(10).toString())!
}
```