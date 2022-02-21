
public class T_CalendarTest {
	public static void main(String[] args) {
		T_Calendar myCalendar = new T_Calendar(13);
		//myCalendar.LAST_MONTH = 13;
		
		//static은 객체를 생성하지 않고도 사용할 수 있다.
		System.out.println(myCalendar.LAST_MONTH);
	}
}
