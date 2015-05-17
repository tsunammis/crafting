// Mutable variable
var myVar :String

// Immutable variable
val myVar :String

// pattern-matching
def toYesOrNo(choice: Int): String = choice match {
  case 1 | 2 | 3 => "yes"
  case 0 => "no"
  case _ => "error"
}

def f(x: Any): String = x match {
  case i:Int => "integer: " + i
  case _:Double => "a double"
  case s:String => "I want to say " + s
}
