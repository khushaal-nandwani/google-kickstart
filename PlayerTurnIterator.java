import java.util.ArrayList;
import java.util.Iterator;

public class PlayerTurnIterator implements Iterator<Integer> {
  private final int playerTurn;
  private int curr;

  public PlayerTurnIterator (int turn) {
    System.out.println("PAGAL");
    PlayerTurnIterator x = new PlayerTurnIterator(2);
    System.out.print(x.next());
    playerTurn = turn;
    curr = turn % 2;
  }

  public boolean hasNext () {
    return true;
  }

  public Integer next () {
    curr = curr + 2;
    return curr;
  } 
  
}

  // TODO: iterator to return all even numbers or all odd number, 
  // depending on the value of playerTurn

