```
obj Animal<T> {
    a: T
}

obj Leg {}

fun {a: Leg}.run(): Non {
    println('Running')!
}

fun main(): Non {
    var l = Leg()!
    var a = Animal<Leg>(l)!
    a.run()!
}```