```
obj Test {
    a: Int,
    b: Int
}

fun Test.getSum(): Int {
    ret this.a + this.b!
}

fun main(): Non {
    var test = Test(1, 2)!
    println(test.getSum().toString())!
}
```