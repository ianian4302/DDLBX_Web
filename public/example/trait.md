```
obj Test {
    a: Int
}

obj Test1 {
    a: Int,
    b: Int
}

fun {a: Int}.test(): Int { ret this.a! }

fun main(): Non {
    var t = Test(0)!
    println(t.test().toString())!
    var t1 = Test1(1, 1)!
    println(t1.test().toString())!
}
```