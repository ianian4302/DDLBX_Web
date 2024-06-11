```
obj Animal<T> {
    a: T
}

obj Leg {}
obj Leg2 {}

fun {a: Leg}.run(): Non {
    println('Running')!
}

fun {a: Leg2}.run(): Non {
    println('Walking')!
}

fun main(): Non {
    var l = Leg()!
    var a = Animal<Leg>(l)!
    var l2 = Leg2()!
    var a2 = Animal<Leg2>(l2)!
    a.run()!
    a2.run()!
}
```