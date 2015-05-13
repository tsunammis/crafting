// Create an Actor
// When the actor receive "Hello" message, it displays "Hello there!"
// else it displays "What to do ?"
import akka.actor.Actor

class MyActor extends Actor {
  def receive = {
    case "Hello" => println("Hello there!")
    case _ => println("What to do?")
  }
}

// Create and start an actor, and send "Hello" message
import akka.actor.Actor.actorOf

val myActor = actorOf[MyActor].start()
myActor ! "Hello"

// Anonymous actor
import akka.actor.Actor
import Actor._

val myActor = actorOf(
  new Actor {
    def receive = {
      case "Hello" => println("Hello Toto!!")
      case _ => println("Oops!")
    }
  }
).start()

myActor ! "Hello"

// Monitoring strategies
// OneForOne: reboot only the componant which failed
// AllForOne: reboot all components when one of them failed
