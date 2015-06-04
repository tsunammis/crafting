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

// Future with callbacks
// http://docs.scala-lang.org/overviews/core/futures.html
// Example #1
import scala.util.{Success, Failure}

val f: Future[List[String]] = future {
  session.getRecentPosts
}

f onComplete {
  case Success(posts) => for (post <- posts) println(post)
  case Failure(t) => println("An error has occured: " + t.getMessage)
}

// Example #2
val f: Future[List[String]] = future {
  session.getRecentPosts
}

f onFailure {
  case t => println("An error has occured: " + t.getMessage)
}

f onSuccess {
  case posts => for (post <- posts) println(post)
}
