package sam04.a1;

import java.util.Calendar;

public class SavedAccount extends Account {
	public void SetValue() {
		date = Calendar.getInstance().getTime();
		name = "은행계좌";
		account_number = 12345;
		//money = 1000; -> 상속받았지만 private는 접근할 수 없음
	}
}
