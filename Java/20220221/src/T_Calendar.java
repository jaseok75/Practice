
public class T_Calendar {
	// final 키워드는 값을 고정하는 역할
	public final int LAST_MONTH;
	
	public T_Calendar(int month) {
		LAST_MONTH = month;	//이렇게 하면 처음 생성자를 실행할 때만 값을 설정할 수 있고 다음부터는 값 못 바꿈
	}
}
