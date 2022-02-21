package exam01;

public class ColledgeStudentTest {
	public static void main(String[] args) {
		ColledgeStudent freshman1 = new ColledgeStudent();
		ColledgeStudent freshman2 = new ColledgeStudent("홍길동");
		ColledgeStudent freshman3 = new ColledgeStudent("홍길동", 20);
		ColledgeStudent freshman4 = new ColledgeStudent("홍길동", 20, "남");
		ColledgeStudent freshman5 = new ColledgeStudent("홍길동", 20, "남", "컴퓨터공학과");
		
		ColledgeStudent freshman6 = new ColledgeStudent("홍길동", "남");
		// 생성자의 매개변수가 같은 인자로 되어 있으면 에러 발생 (오버로딩)
		//ColledgeStudent freshman7 = new ColledgeStudent("홍길동", "컴퓨터공학과");
		
	}
}