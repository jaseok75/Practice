package exam01;

public class CreditCard {
	private long cardNumber;
	public String cardOwner;
	public long totalMoney;
	private long point;
	
	public void useCard(long useMoney) {
		totalMoney += useMoney;
	}
	
	public void payCardMoney(long payMoney) {
		totalMoney -= payMoney;
		point(payMoney / 1000);
	}
	
	private void point(long point) {
		this.point += point;
	}
	
	public void setCardNumber(long cardNumber) {
		this.cardNumber = cardNumber;
	}
	
	public long getCardNumber() {
		return cardNumber;
	}
}
