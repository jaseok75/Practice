
public class Cola {
	//명시적 초기화: 변수를 할당할 때 값을 함께 설정
	private static int capacity = 20;
	private int date = 10;
	
	static {
		System.out.println(" 클래스 초기화 블럭 ");
		//date = 40;	//error
		capacity = 40;
		System.out.println("capacity:" + capacity);
	}
	
	{
		System.out.println(" 인스탄스 초기화 블럭 ");
		date = 50;
		capacity = 50;
		System.out.println("capacity:" + capacity);
		System.out.println("capacity:" + date);
	}
	
	public Cola() {
		System.out.println(" 생성자 호출 ");
		capacity = 60;
		date = 60;
		System.out.println("capacity:" + capacity);
		System.out.println("capacity:" + date);
	}
}
