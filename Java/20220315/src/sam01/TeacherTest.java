package sam01;

public class TeacherTest {
	public static void main(String[] args) {
		Teacher abc = new Teacher("김사람", 1111, "테스트캠퍼스", 2222);
		
		System.out.println("---------------------------");
		System.out.println("이름: " + abc.name);
		System.out.println("주민번호: " + abc.getNumber());
		System.out.println("학교명: " + abc.schoolName);
		System.out.println("교원번호: " + abc.number);
		
		Person person1 = abc; // 업캐스팅
		
		System.out.println("---------------------------");
		System.out.println("이름: " + person1.name);
		System.out.println("주민번호: " + person1.number);
	}
}
