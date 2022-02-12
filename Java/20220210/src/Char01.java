
public class Char01 {
	public static void main(String[] args) {
		CreditCard card = new CreditCard();
		//card.cardNumber = 1111_2222_3333_4444L;
		card.setCardNumber(1111_2222_3333_4444L);
		card.cardOwner = "Kim Ha Rim";
		
		System.out.println(card.getCardNumber());
		System.out.println(card.cardOwner);
		
		card.useCard(1000);
		
		System.out.println(card.totalMoney);
	}
}