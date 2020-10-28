class Q3{
  public static void main(String[] args){
    String myStr1 = "Hello";
    String myStr1 = "World";
    System.out.println(myStr1.charAt(0)); //H
    
    System.out.println(myStr1.contains("Hel")); //true
    System.out.println(myStr2.contains("Hel")); //false
    
    System.out.println(myStr1.endsWith("Hel")); //true
    System.out.println(myStr1.endsWith("lo")); //false
    
    System.out.println(myStr1.indexOf("l")); //2
    System.out.println(myStr2.endsWith("rl")); //2
    
    System.out.println(myStr1.length()); // 5
    
    System.out.println(myStr1.toUpperCase()); //HELLO
    
    System.out.println(myStr2.toLowerCase()); //WORLD
    
  }
}
