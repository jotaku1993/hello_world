import java.io.*;

//to read the input from the terminal
class GameHelper{
	public String getUserInput(String prompt){
		String inputLine = null;
		System.out.print(prompt+"  ");
		try{
			BufferedReader is = new BufferedReader(
				new InputStreamReader(System.in));
			inputLine = is.readLine();
			if (inputLine.length()==0) return null;
		} catch (IOException e){
			System.out.println("IOException: " + e);
		}
		return inputLine;
	}
}

//game sample
class SimpleDotCom{
	int[] locationCells;
	int numOfHits=0;

	public void setLocationCells(int[] locs){
		locationCells = locs;
	}

	public String checkYourself(String stringGuess){
		int guess = Integer.parseInt(stringGuess);
		String result = "miss";

		for (int cell:locationCells){
			if (guess==cell){
				result = "hit";
				numOfHits++;
				break;
			}
		}
		if (numOfHits == locationCells.length){
			result = "kill";
		}
		System.out.println(result);
		return result;
	}
}

//game launcher
public class test{
	public static void main(String [] args){
		int numOfGuesses = 0;
		GameHelper helper = new GameHelper();

		SimpleDotCom dot = new SimpleDotCom();

		int temp = (int)(Math.random()*5);
		int[] locations = {temp,temp+1,temp+2};
		dot.setLocationCells(locations);

		boolean isAlive = true;

		while(isAlive==true){
			String guess = helper.getUserInput("enter a number(from 0~7)");
			String result = dot.checkYourself(guess);
			numOfGuesses++;
			if (result.equals("kill")){
				isAlive = false;
				System.out.println("You took "+ numOfGuesses + " guesses");
			}
		}
	}
}