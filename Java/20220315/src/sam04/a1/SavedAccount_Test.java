package sam04.a1;

import java.util.Calendar;

public class SavedAccount_Test {
	public static void main(String[] args) {
		Account account1 = new Account();
		account1.name = "은행 계좌";
		account1.date = Calendar.getInstance().getTime();
		account1.account_number = 12345;
		//account1.money = 1000; -> Error (private는 접근할 수 없음)
	}
}
