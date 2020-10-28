import javax.swing.*;
class Q4{
  public static void main(String[] args){
    frame = new JFrame();
    String str = JOptionPane.showInputDialog(frame, "Enter a String: ");
    
    JOptionPane.showMessageDialog(frame,"Character at index 0: "+str.charAt(0));
    
     JOptionPane.showMessageDialog(frame,"String contains Hel?: "+str.contains("Hel"));
    
     JOptionPane.showMessageDialog(frame,"String Ends with Hel?:  " + str.endsWith("Hel"));
    
     JOptionPane.showMessageDialog(frame,"Index of First Occurence l: "+str.indexOf("l"));
    
     JOptionPane.showMessageDialog(frame,"String length: "+str.length());
    
     JOptionPane.showMessageDialog(frame,"Upper Case string: "+str.toUpperCase());
    
     JOptionPane.showMessageDialog(frame,"Lower Case String: "+str.toLowerCase());
    
  }
}
