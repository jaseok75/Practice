package sam04.a2;

import java.util.Calendar;

import sam04.a1.Account;

public class SavedAccountCheck extends Account {
	public void CheckValue() {
		name = "저축계좌";
		date = Calendar.getInstance().getTime();
	}
}
