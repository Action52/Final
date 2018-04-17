/*
  Luis Alfredo León Villapún A01322275
  Armando Canto García A01322361
*/

import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		for (int i = 0;i < n ;i++ ) {
			double aX = input.nextDouble();
			double aY = input.nextDouble();
			double bX = input.nextDouble();
			double bY = input.nextDouble();
			double cX = input.nextDouble();
			double cY = input.nextDouble();
			double aux = (aX*bY-aY*bX+ bX*cY-bY*cX+ cX*aY-cY*aX)/2;
			if (aux < 0) {
        aux = -aux;
      }
			aux /= 7;
			aux += 0.5;
			System.out.println((int)aux);
		}
	}
}
