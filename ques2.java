public class ques2 {
  public static int tripleFactorial(int n) {
    int mod  = 1000000007;
    int ans = 1;
    while(n>0) {
      ans = (ans * n)%mod;
      n-=3;
    }
    return ans;
  }

  public static void main(String args[]) {
    System.out.println(tripleFactorial(50));
  }
}
