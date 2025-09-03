public class ques1 {
  public static int candyGame(int x, int y) {
  
    while(x!=0 && y!=0 && x!=y) {
      if (x<y) {
        y = y - x;
      } else if (y<x) {
        x = x - y;
      }
    }
    
    return x+y;
  }

  public static void main(String args[]) {
    System.out.println(candyGame(10, 5));
  }
}
