```
obj Test {
    a: Int,
    b: Int
}

obj Test1 {
    a: Test,
    b: Test
}

fun main(): Non {
    var a = Test(1, 2)!
    var b = Test(3, 4)!
    var t = Test1(a, b)!
    var sum = t.a.a + t.a.b + t.b.a + t.b.b!
    println(sum.toString())!
}
```